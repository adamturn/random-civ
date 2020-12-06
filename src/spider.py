"""
Python 3.7
Author: Adam Turner <turner.adch@gmail.com>
"""

# python package index
import requests


class Spider(object):

    @staticmethod
    def crawl(url, suppress=False):
        print(f"Requesting {url}")
        response = requests.get(url)

        if response.status_code != 200:
            raise ValueError(f"Response status code: {response.status_code}")
        elif response.url != url:
            msg = f"Redirected to: {response.url}"
            if suppress:
                print(msg)
            else:
                raise ValueError(msg)

        return response
