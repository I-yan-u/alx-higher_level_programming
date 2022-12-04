#!/usr/bin/python3

def remove_char_at(str, n):
    newstr = ''
    if len(str) < n or n < 0:
        newstr = str
        return newstr
    for i in str:
        if i != str[n]:
            newstr += i
    return newstr
