#!/usr/bin/python3
"""
    2-append_write: append_write()
"""


def append_write(filename="", text=""):
    """
        Open a .txt file
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        char_lenght = 0
        for words in text:
            for char in words:
                char_lenght += 1
        return char_lenght
