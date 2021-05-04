#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cop = my_list[:]
    if idx < 0:
        return cop
    elif idx >= len(my_list):
        return cop
    else:
        cop[idx] = element
        return cop
