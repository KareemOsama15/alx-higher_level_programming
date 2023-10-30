#!/usr/bin/python3

"""
This module is for Rectangle class.
"""


class Rectangle:
    """class that defines a Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        method that initialize the instances.

        Args:
            width: width of the rectangle
            height: heigtht of the rectangle


        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        method that returns the rectangle area.

        Returns:
            rectangle area

        """
        return (self.width * self.height)

    def perimeter(self):
        """
        method that returns the rectangle perimeter.

        Returns:
            rectangle perimeter

        """
        rec_perimeter = (self.width + self.height) * 2
        return (rec_perimeter)

    def __str__(self):
        """
        method that print the rectangle with the character #

        Returns:
            no return

        """

        rectangle = ''

        if self.height == 0 or self.width == 0:
            return (rectangle)
        for i in range(self.height):
            rectangle += ('#' * self.width) + '\n'
        return (rectangle[:-1])

    def __repr__(self):
        """
        method that return a string representation of the rectangle

        Returns:
            string representation of an object

        """

        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """
        method that print a massage when instance is delete

        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
