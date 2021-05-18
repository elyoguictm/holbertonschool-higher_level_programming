#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Defines a Square."""

    def __init__(self, size=0):
        """Init Square."""
        self.size = size

    @property
    def size(self):
        """Return Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets Square with a size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return square area."""
        return self.__size * self.__size

    def my_print(self):
        """prints the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
                print("#" * self.__size)
