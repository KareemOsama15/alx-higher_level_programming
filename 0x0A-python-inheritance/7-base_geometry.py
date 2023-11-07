#!/usr/bin/python3

"""This module is for BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class is defines an object"""

    def area(self):
        """
        method that raises an Exception massage
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method that validates value.

        Args:
            name: a string
            value: should be aan integer

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less or equal to zero
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
