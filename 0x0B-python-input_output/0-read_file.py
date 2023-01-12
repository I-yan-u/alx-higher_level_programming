#!/usr/bin/python3
"""
    0-read_file: read_file()
"""


def read_file(filename=""):
    """
        Open a .txt file
    """
    with open(filename, "r", encoding="utf-8") as file:
        line = file.read()
        print(line)
