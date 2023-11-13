#!/usr/bin/python3
"""This module for Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """method that initialize class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """method that gets size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """method that sets size"""
        self.width = value
        self.height = value

    def __str__(self):
        """str method"""
        return ("[Square] ({}) {}/{} {}".format(self.id, self.x, self.y,
                                                self.width))

    def update(self, *args, **kwargs):
        """method that assigns attributes"""
        if len(args) != 0 and args is not None:
            keysList = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if keysList[i] == "size":
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, keysList[i], args[i])
        else:
            for dictKey, dictValue in kwargs.items():
                if dictKey == "size":
                    setattr(self, "width", dictValue)
                    setattr(self, "height", dictValue)
                else:
                    setattr(self, dictKey, dictValue)

    def to_dictionary(self):
        """method returns the dictionary representation of a Rectangle"""
        dickKeys = ["id", "x", "size", "y"]
        newDict = {}
        for key in dickKeys:
            if key == "size":
                newDict[key] = getattr(self, "width")
            else:
                newDict[key] = getattr(self, key)
        return (newDict)
