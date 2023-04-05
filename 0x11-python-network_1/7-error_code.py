#!/usr/bin/python3
"""
Get header details for address in sys.argv[1]
Using requests
"""
import requests as re
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = re.get(url)
        print(response.text)
        response.raise_for_status()
    except re.exceptions.HTTPError as errors:
        print("Error code: {}".format(errors.response.status_code))
