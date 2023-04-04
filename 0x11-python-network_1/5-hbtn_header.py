#!/usr/bin/python3
"""
Get header details for address in sys.argv[1]
Using requests
"""
import requests as re
import sys


if __name__ == "__main__":
    response = re.get(sys.argv[1])

    print(dict(response.headers).get("X-Request-Id"))