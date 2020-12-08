"""
Python 3.7
Author: Adam Turner <turner.adch@gmail.com>
"""

# python package index
import lxml.html
import pandas as pd
# standard library
import os


class Wrangler(object):

    @staticmethod
    def __process_multiciv(data, civs, leaders):
        """Process leaders with multiple civs."""
        for i, element in enumerate(data):
            # Eleanor of Aquitaine can be either English or French
            if element.startswith("Eleanor"):
                leaders.append(data.pop(i))
                civs.append(f"{data.pop(i)}, {data.pop(i)}")

        return data, civs, leaders

    @staticmethod
    def __write_records(records, data_dir):
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
        write_path = str(data_dir / "records.csv")
        print(f"Writing data to {write_path}")
        df = pd.DataFrame.from_records(records)
        df.to_csv(write_path, index=False)

        return None

    @staticmethod
    def read_records(data_dir):
        file_path = str(data_dir / "records.csv")
        print(f"Reading data from {file_path}")
        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError as e:
            print(f"WARNING: Could not find {file_path}! Try passing 'main.py update'.")
            raise e

        return df.to_records(index=False)

    @staticmethod
    def process_html(request_response, data_dir):
        doc = lxml.html.fromstring(request_response.content)
        elements = doc.xpath("//td/a//text()")

        data = [str(element) for element in elements]
        civs, leaders = [], []
        data, civs, leaders = Wrangler.__process_multiciv(data, civs, leaders)

        # expects data to be arranged in nx2 array captured by xpath expression
        # with any leaders that have multiple civs already processed
        if (len(data) % 2) != 0:
            raise ValueError(f"Data is uneven! Data: {data} Civs: {civs} Leaders: {leaders}")
        else:
            for i in range(len(data)):
                if (i % 2) == 0:
                    leaders.append(data[i])
                else:
                    civs.append(data[i])

        records = [(leader, civ) for leader, civ in zip(leaders, civs)]
        Wrangler.__write_records(records, data_dir)

        return records
