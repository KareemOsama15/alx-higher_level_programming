#!/usr/bin/python3
"""This module is for MyInt class"""


class MyInt(int):
    """
    class that inherits from class int
    """

    def __ne__(self, __value):
        """method that returns True if equal"""

        return super().__eq__(__value)

    def __eq__(self, __value):
        """method that returns False if equal"""

        return super().__ne__(__value)
