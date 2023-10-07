#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        i = 0
        for item in list:
            print("{:d}".format(item), end=(" " if i < len(list) - 1 else ""))
            i += 1
        print()
