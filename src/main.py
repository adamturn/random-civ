"""
Python 3.7
Author: Adam Turner <turner.adch@gmail.com>
"""

# standard library
import sys
import random
import pathlib
# local modules
from spider import Spider
from process_data import Wrangler


def update(data_dir):
    print("Crawling...")
    url = "https://civilization.fandom.com/wiki/Leaders_(Civ6)"
    response = Spider.crawl(url)

    print("Processing html...")
    records = Wrangler.process_html(response, data_dir)

    return records


def main(data_dir, records=False):
    if not records:
        records = Wrangler.read_records(data_dir)

    loop = True
    while loop:
        n = int(input("\nSelect how many Civs? n = "))
        for i in range(n):
            record = random.choice(records)
            print(f"{i+1}. {record[0]} ({record[1]})")

        answer = input("\nTry again? [y]/n: ")
        if answer in ("n", "q"):
            loop = False
            print("Exiting program...")
        else:
            continue

    return None


if __name__ == "__main__":
    src_dir = pathlib.Path(__file__).parent.absolute()
    data_dir = src_dir.parent / "data"

    if sys.argv[-1] == "update":
        main(data_dir, records=update(data_dir))
    else:
        main(data_dir)
