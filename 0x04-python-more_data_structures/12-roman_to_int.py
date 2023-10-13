#!/usr/bin/python3

def roman_to_int(roman_string):

    if not roman_string:
        return (0)

    romVal = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    num = 0
    romStr = roman_string[:]

    for i in range(len(romStr)):
        if i < len(romStr) - 1 and romVal[romStr[i]] < romVal[romStr[i + 1]]:
            num -= romVal[romStr[i]]
        else:
            num += romVal[romStr[i]]
    return (num)
