#!/usr/bin/python3

class Square:
    """Class Square that defines a square object
    """
    def __init__(self, size=0):
        """Method that initialize object attributes
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method that returns the area of a square object
        """
        return (self.__size ** 2)
