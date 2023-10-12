#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    else:
        num = 0
        sum = 0
        for tuple in my_list:
            sum += tuple[0] * tuple[1]
            num += tuple[1]
        return (sum / num)
