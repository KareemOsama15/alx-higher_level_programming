#!/usr/bin/python3
"""module of function find_peak"""


def find_peak(list_of_integers):
    """function that finds a peak of list of unsorted integers"""
    if not list_of_integers:
        return None
    low = 0
    high = len(list_of_integers) - 1
    while low < high:
        mid = (low + high)//2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return list_of_integers[low]
