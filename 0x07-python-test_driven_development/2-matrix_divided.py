#!/usr/bin/python3

def matrix_divided(matrix, div):

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
