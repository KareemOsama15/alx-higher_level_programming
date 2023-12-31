#!/usr/bin/python3

"""
This module is for Rectangle class.
"""


class Rectangle:
    """class that defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        method that initialize the instances.

        Args:
            width: width of the rectangle
            height: heigtht of the rectangle


        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        method that gets the value of width.

        Returns:
            width of rectangle

        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """
        method that sets the value of width.

        Args:
            value: value of rectangle width

        Raises:
            TypeError: if width not integer
            ValueError: if width is less than 0

        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        method that gets the value of height.

        Returns:
            height of rectangle

        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """
        method that sets the value of height.

        Args:
            value: value of rectangle height

        Raises:
            TypeError: if height not integer
            ValueError: if height is less than 0

        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
