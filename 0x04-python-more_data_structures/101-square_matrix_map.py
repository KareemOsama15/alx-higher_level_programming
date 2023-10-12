#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda sqnum: list(map(lambda x: x ** 2, sqnum)), matrix))
