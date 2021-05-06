#!/usr/bin/python3
def uniq_add(my_list=[]):
    neww = []
    tot = 0
    for i in range(len(my_list)):
        if my_list[i] not in neww:
            neww.append(my_list[i])
    return sum(neww)
