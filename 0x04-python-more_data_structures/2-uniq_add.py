#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    temp = []
    for num in my_list:
        if num not in temp:
            total += num
            temp.append(num)
        else:
            pass
    return total
