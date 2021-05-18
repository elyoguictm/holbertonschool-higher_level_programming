#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Defines a Square."""

    def __init__(self, size=0):
        """Init Square with a size."""
        if size != int(size):
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
