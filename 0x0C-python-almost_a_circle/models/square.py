#!/usr/bin/python3
"""
Contains the "Square" class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string represent"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    @property
    def size(self):
        """size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """key values"""
        if args and len(args):
            for i, elm in enumerate(args):
                if i == 0:
                    self.id = elm
                elif i == 1:
                    self.size = elm
                elif i == 2:
                    self.x = elm
                elif i == 3:
                    self.y = elm
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """return dict"""
        square_dict = {}
        square_dict["id"] = self.id
        square_dict["size"] = self.size
        square_dict["x"] = self.x
        square_dict["y"] = self.y
        return square_dict
