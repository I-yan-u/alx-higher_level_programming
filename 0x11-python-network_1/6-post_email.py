#!/usr/bin/python3
"""
Get header details for address in sys.argv[1]
Using requests
"""
import requests as re
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    response = re.post(url, data=email)

    print(response.text)
