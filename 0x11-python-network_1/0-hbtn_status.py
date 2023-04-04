#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status.
"""
import urllib.request as ur


if __name__ == "__main__":
    req = ur.Request('https://alx-intranet.hbtn.io/status')
    with ur.urlopen(req) as response:
        cont = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(cont)))
        print("\t- content: {}".format(cont))
        print("\t- utf8 content: {}".format(cont.decode("utf-8")))