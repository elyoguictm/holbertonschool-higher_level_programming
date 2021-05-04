#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for z in matrix:
        for x in z:
            print("{:d}".format(x), end=" " if x != z[-1] else "")
        print()
