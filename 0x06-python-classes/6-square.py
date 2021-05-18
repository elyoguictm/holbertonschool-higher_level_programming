#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Defines a Square."""

    def __init__(self, size=0, position=(0, 0)):
        """init the square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns Square size"""
        return self.__size

    @property
    def position(self):
        """Returns Square position."""
        return self.__position

    @size.setter
    def size(self, value):
        """Sets Square with a size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Sets Square with a position."""
        if type(value) is not tuple or len(value) is not 2\
                or type(value[0]) is not int or type(value[1]) is not int\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """prints the square with the character #."""
        if self.__size == 0:
            print()
            return
        if self.__position == (0, 0):
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                if self.__position[0] != 0:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)
