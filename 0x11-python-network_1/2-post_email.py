#!/usr/bin/python3
"""
Post email provided in argv[2] to url in argv[1]
"""
import urllib.request as ur
import urllib.parse as up
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    data = up.urlencode(val).encode("ascii")

    req = ur.Request(url, data)
    with ur.urlopen(req) as response:
        print(response.read().decode(encoding="utf-8"))
