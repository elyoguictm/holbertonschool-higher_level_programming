#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cont = 0
    for z in range(x):
        try:
            print(my_list[z], end="")
            cont += 1
        except IndexError:
            print()
            return cont
    print()
    return cont
