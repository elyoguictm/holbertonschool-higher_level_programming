#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    neww = a_dictionary
    neww.pop(key, None)
    return neww
