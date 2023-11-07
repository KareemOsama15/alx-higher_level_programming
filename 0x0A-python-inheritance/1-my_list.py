#!/usr/bin/python3

"""
this module is for class
"""


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
