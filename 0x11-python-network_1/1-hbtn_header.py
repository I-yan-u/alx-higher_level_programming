#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status.
"""
import urllib.request as ur
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = ur.Request(url)
    with ur.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
