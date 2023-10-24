#!/usr/bin/python3
class Square:
    """Class Square that defines a square object
    """
    def __init__(self, size=0, position=(0, 0)):
        """Method that initialize object attributes
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Method that returns the object position value
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Method that sets the position value of a square object
        """
        if not isinstance(value, tuple) or len(value) > 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method that returns the area of a square object
        """
        return (self.__size ** 2)

    def my_print(self):
        """Method that prints "#" and ' ' of a square object
        accroding to its size and position
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)
            if self.position[1] > 0:
                print()
