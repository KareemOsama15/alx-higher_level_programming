#!/usr/bin/python3

"""This module is for Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from class Rectangle"""

    def __init__(self, size):
        """method that initialize object from class Square"""

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """method that returns the area of an object of Square class"""

        return (super().area())
