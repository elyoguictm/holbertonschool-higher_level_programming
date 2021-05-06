#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    number = 0
    d = 0
    for t in my_list:
        number += t[0] * t[1]
        d += t[1]
    return number / d
