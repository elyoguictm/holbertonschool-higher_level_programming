#!/usr/bin/python3
"""BaseGeometry module"""
Rectangle = __import__('9-rectangle').Rectangle

"""Square"""


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of square"""
        return self.__size ** 2
