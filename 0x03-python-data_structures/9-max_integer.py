#!/usr/bin/python3
def replace(list_=[], num=0):
    if len(list_) == 0:
        list_.append(num)
    else:
        del list_[0]
        list_.append(num)
    return list_

def max_integer(my_list=[]):
    idx = 0
    idx2 = idx + 1
    temp = []
    for numbers in my_list:
        if idx2 > idx:
            replace(temp, my_list[idx2])
    return temp[0]
