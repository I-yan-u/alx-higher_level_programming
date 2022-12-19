#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_l = []
    for x in range(list_length):
        try:
            result_l.append(my_list_1[x]/my_list_2[x])
        except ZeroDivisionError:
            result_l.append(0)
            print("division by 0")
        except TypeError:
            result_l.append(0)
            print("wrong type")
        except IndexError:
            result_l.append(0)
            print("out of range")
        finally:
            pass
    return result_l
