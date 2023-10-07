#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    else:
        maxNum = my_list[0]
        for i in range(len(my_list)):
            if maxNum < my_list[i]:
                maxNum  = my_list[i]
        return (maxNum)
