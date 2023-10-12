#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    newMatrix = []
    for list in matrix:
        subMatrix = []
        for j in range(len(list)):
            subMatrix.append(list[j] ** 2)
        newMatrix.append(subMatrix)
    return (newMatrix)
