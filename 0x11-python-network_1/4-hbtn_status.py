#!/usr/bin/python3
"""
fetches status file from https://alx-intranet.hbtn.io/status
Using requests
"""
import requests as re


if __name__ == "__main__":
    request = re.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))
