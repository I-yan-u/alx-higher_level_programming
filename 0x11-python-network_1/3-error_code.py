#!/usr/bin/python3
"""
Requests from add provided at sys.argv[1].
Handles HTTP errors
"""
import urllib.request as ur
import urllib.error as ue
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = ur.Request(url)

    try:
        with ur.urlopen(req) as response:
            print(response.read().decode(encoding="utf-8"))
    except ue.HTTPError as e:
        print("Error code: {}".format(e.code))
