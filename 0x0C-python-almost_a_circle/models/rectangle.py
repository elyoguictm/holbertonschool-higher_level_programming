#!/usr/bin/python3
"""
Contains the "Rectangle" class
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init rect"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area width height"""
        return self.__width * self.__height

    def display(self):
        """print charact#"""
        for i in range(0, self.__y):
            print()
        print(((' ' * self.__x) + ('#' * self.__width + '\n')) *
              self.__height, end="")

    def __str__(self):
        """string represent rect"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """key value"""
        if args and len(args):
            for i, elm in enumerate(args):
                if i == 0:
                    self.id = elm
                elif i == 1:
                    self.width = elm
                elif i == 2:
                    self.height = elm
                elif i == 3:
                    self.x = elm
                elif i == 4:
                    self.y = elm
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """return dictonary"""
        rectangle_dict = {}
        rectangle_dict["id"] = self.id
        rectangle_dict["width"] = self.width
        rectangle_dict["height"] = self.height
        rectangle_dict["x"] = self.x
        rectangle_dict["y"] = self.y
        return rectangle_dict
