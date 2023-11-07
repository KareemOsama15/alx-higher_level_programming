#!/usr/bin/python3

"""This module is for class MyList"""


class MyList(list):
    """
    class that inherits from list class
    """

    def print_sorted(self):
        """
        method that prints the list, but sorted (ascending sort)
        """

        sortedList = self.copy()
        sortedList.sort()
        print(sortedList)
