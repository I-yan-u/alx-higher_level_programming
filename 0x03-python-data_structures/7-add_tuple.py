#!/usr/bin/python3
def des_tuple(tuple_=()):
    tuple_len = len(tuple_)
    if tuple_len == 0:
        return (0, 0)
    elif tuple_len == 1:
        return (tuple_[0], 0)
    else:
        return (tuple_[0], tuple_[1])



def add_tuple(tuple_a=(), tuple_b=()):
    sum_1 = 0
    sum_2 = 0
    tup1 = des_tuple(tuple_a)
    tup2 = des_tuple(tuple_b)
    sum_1 = tup1[0] + tup2[0]
    sum_2 = tup1[1] + tup2[1]
    return (sum_1, sum_2)
