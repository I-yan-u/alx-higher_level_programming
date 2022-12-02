#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    argc = len(argv)

    sum1 = 0
    if argc == 1:
        print(sum1)
    else:
        for i in range(1, argc):
            sum1 += int(argv[i])
        print(sum1)
