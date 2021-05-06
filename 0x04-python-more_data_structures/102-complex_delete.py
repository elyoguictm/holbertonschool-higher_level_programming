#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = dict(a_dictionary)
    for key, val in tmp.items():
        if val == value:
            del a_dictionary[key]
    return a_dictionary
