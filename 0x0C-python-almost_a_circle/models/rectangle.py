#!/usr/bin/python3
"""This module for class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method that initialize Rectangle class objects"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """method gets width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """method sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """method gets height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """method that sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """method gets x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """method sets x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """method gets y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """method sets y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method that return the area of a rectangle object"""
        return (self.width * self.height)

    def display(self):
        """method that prints in stdout the Rectangle instance with char #"""
        print("\n" * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """str method"""
        return ("[Rectangle] ({}) {}/{} {}/{}".format(self.id, self.x, self.y,
                                                      self.width, self.height))

    def update(self, *args, **kwargs):
        """method that assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            argsList = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, argsList[i], args[i])
        else:
            for dictKey, dictValue in kwargs.items():
                setattr(self, dictKey, dictValue)

    def to_dictionary(self):
        """method returns the dictionary representation of a Rectangle"""
        dictKeys = ['x', 'y', 'id', 'height', 'width']
        newDict = {}
        for key in dictKeys:
            newDict[key] = getattr(self, key)
        return (newDict)
