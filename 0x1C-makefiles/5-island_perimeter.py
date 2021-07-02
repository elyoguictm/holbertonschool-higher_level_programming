#!/usr/bin/python3
"""Perimeter of the island described in grid"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    perim = 0
    for z in grid:
        for x in row:
            if x == 1:
                perim += 2
    if perim > 0:
        perium += 2
    return perim
