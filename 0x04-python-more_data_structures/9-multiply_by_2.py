#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newww = {}
    for key, value in a_dictionary.items():
        newww[key] = value * 2
    return newww
