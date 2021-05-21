#!/usr/bin/python3
"""This module contain add_integer method."""


def add_integer(a, b=98):
    """
    Args:
        a: The first integer.
        b: The second integer, default 98.
    Raise:
        TypeError if a or b are not integers or floats.
    Return:
        The addition of the two given integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return (int(a) + int(b))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
