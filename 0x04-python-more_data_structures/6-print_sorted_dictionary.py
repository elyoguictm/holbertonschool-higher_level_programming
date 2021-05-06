#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for z in sorted(a_dictionary.keys()):
        print("{}: {}".format(z, a_dictionary[z]))
