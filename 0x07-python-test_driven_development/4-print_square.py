#!/usr/bin/python3
""" Print square" module """


def print_square(size):
    """
        Args:
            size (int): size of a side of the square
        Raises:
            TypeError: in case size is not int.
            ValueError: in case size less than 0.
        Return:
            Nope
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        print(("#" * size + '\n') * size, end="")
