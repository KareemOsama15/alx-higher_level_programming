#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    else:
        num = 0
        sum = 0
        for tupl in my_list:
            sum += tupl[0] * tupl[1]
            num += tupl[1]
        return (sum / num)
