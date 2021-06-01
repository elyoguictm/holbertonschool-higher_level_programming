#!/usr/bin/python3
"""Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """def area"""
        return self.__size * self.__size

    def __str__(self):
        """square area"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
