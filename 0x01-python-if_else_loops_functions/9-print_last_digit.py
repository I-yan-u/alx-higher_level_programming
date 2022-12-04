#!/usr/bin/python3
def ab(number):
    if number < 0:
        return (-1 * number)


def print_last_digit(number):
    if number >= 0:
        n = number % 10
        print("{:d}".format(n), end='')
    else:
        pos = ab(number)
        n = pos % 10
        print("{:d}".format(n), end='')
    return n
