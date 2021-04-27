#!/usr/bin/python3
for z in range(0, 100):
    if z == 0 or (z/10 >= z % 10):
        continue
    elif (z < 89):
        print("{:02d}, ".format(z), end="")
    else:
        print("{:02d}".format(z))
