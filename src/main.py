# Python 3.8.5 64-bit ('civ': conda)
# Author: Adam Turner <turner.adch@gmail.com>

# standard library
import re
import random
# conda repo
import requests
import pandas as pd
import lxml.html as lh


def main():
    url = 'https://civilization.fandom.com/wiki/Leaders_(Civ6)'
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    rows = doc.xpath('//tr')
    rows = [row for row in rows if len(row) == 4]
    header = rows[0]
    rows = rows[1:]

    # first two columns of data: Leader, Civ
    cols = list()
    for i in range(2):
        element = header[i].text_content().strip()
        cols.append(element)
    print(cols)

    regex = re.compile(r"\[\d{1,2}\]")
    data = list()
    for row in rows:
        pair = list()
        for i in range(2):
            content = row[i].text_content().strip()
            content = regex.sub("", content)
            pair.append(content)
        data.append(tuple(pair))

    df = pd.DataFrame(data, columns=cols)

    breakpoint()

    while True:
        n = input("[user] n = ")
        for _ in range(int(n)):
            civ = random.choice(data)
            print(f"{civ[0]} ({civ[1]})")
        cont = input("Continue? [y]/n: ")
        breakpoint()
        if cont == 'n' or 'q':
            break

    return None


if __name__ == "__main__":
    main()
