#!/usr/bin/python3

"""This module is for Rectangle class that inherits from BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """method that defines Rectangle instances"""

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """method that returns area of an object of /Rectangle class"""

        return (self.__width * self.__height)

    def __str__(self):
        """method that prints specified formation"""

        return (f"[Rectangle] {self.__width}/{self.__height}")
