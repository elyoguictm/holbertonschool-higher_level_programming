#!/usr/bin/python3
for z in range(97, 123):
    if (z == 101 or z == 113):
        continue
    print("{}".format(chr(z)), end="")
