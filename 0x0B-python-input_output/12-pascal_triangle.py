#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """pascal traingle"""

    pascal = []
    if n > 0:
        for z in range(n):
            row = []
            row.append(1)
            x = 0
            while x < (z - 1):
                row.append(pascal[z - 1][x] + pascal[z - 1][x + 1])
                x += 1
            if z != 0:
                row.append(1)
            pascal.append(row)
    return pascal
