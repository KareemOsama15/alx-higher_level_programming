#!/usr/bin/python3
"""This module is for function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements (int, floats)of a matrix.

    Args:
        matrix: list of lists
        div: number that divides the matrix

    Returns:
        new matrix with new elements divided by div

    Raises:
        TypeError: if matrix item isn't integers/floats
                   if matrix lists didin't have same size
                   if div isn't an integer or float
        ZeroDivision: if div is equal zero

    """

    type_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(type_msg)

    lenList = len(matrix[0])
    for lst in matrix:
        if not isinstance(lst, list):
            raise TypeError(type_msg)

        for item in lst:
            if not type(item) in (int, float):
                raise TypeError(type_msg)

        if lenList != len(lst):
            raise TypeError("Each row of the matrix must have the same size")
        lenList = len(lst)

    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    newMatrix = []
    for lst in matrix:
        newList = []
        for item in lst:
            newList.append(round(item / div, 2))
        newMatrix.append(newList)
    return (newMatrix)
