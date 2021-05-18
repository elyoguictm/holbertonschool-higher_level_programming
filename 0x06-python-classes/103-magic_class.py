#!/usr/bin/python3
"""Magic Class."""
import math


class MagicClass:
    """ Magic Class """

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    """ Definir area """
    def area(self):
        return self.__radius ** 2 * math.pi

    """ Definir circunference"""
    def circumference(self):
        return 2 * math.pi * self.__radius
