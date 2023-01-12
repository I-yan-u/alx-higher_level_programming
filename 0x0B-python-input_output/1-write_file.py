#!/usr/bin/python3
"""
    1-write_file: write_file()
"""


def write_file(filename="", text=""):
    """
        Open a .txt file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        char_lenght = 0
        for words in text:
            for char in words:
                char_lenght += 1
        return char_lenght
