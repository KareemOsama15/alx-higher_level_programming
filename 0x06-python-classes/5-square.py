#!/usr/bin/python3
class Square:
    """Class Square that defines a square object
    """
    def __init__(self, size=0):
        """Method that initialize object attributes
        """
        self.size = size

    @property
    def size(self):
        """Method that returns the object size value
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Method that sets the size value of a square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method that returns the area of a square object
        """
        return (self.__size ** 2)

    def my_print(self):
        """Method that prints "#" of a square object
        accroding to its size
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print('#' * self.size)
