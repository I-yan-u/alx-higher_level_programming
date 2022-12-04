#!/usr/bin/python3
def uppercase(str1):
    new = ""
    for c in str1:
        if ord(c) in range(97, 123):
            new += chr(ord(c)-32)
        else:
            new += c
    print("{}".format(new))
