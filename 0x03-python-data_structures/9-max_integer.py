#!/usr/bin/python3
def size_check(list_=[], num=0):
    if len(list_) == 0:
        list_.append(num)
    else:
        if list_[0] >= num:
            return list_
        else:
            del list_[0]
            list_.append(num)
    return list_


def max_integer(my_list=[]):
    lent = len(my_list)
    temp = []
    if lent == 0:
        return None
    for idx in range(lent):
        size_check(temp, my_list[idx])
    return temp[0]
