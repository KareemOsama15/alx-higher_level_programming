#!/usr/bin/python3

"""
here I want to get the real number printing on screen,
    so uses 2 diff variables (count, i)
count => to print real element printed because it will pass in some cases
i => to get the value of idex if was valid
    , and to handle if x bigger than list length
"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except TypeError:
            pass
        except ValueError:
            pass
        i += 1
    print()
    return (count)
