#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        listLen = len(my_list) - 1
        for i in range(listLen, -1, -1):
            print("{:d}".format(my_list[i]))