#!/usr/bin/python3

for z in range(122, 96, -1):
    x = 32 if (z % 2 != 0) else 0
    print("{}".format(chr(z - x)), end="")
