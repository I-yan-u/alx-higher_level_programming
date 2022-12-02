#!/usr/bin/python3.8

if __name__ == '__main__':
    import hidden_4 as hidden

    lent = len(dir(hidden))
    lst = dir(hidden)
    for i in range(lent):
        if "__" in lst[i]:
            pass
        else:
            print(lst[i])
