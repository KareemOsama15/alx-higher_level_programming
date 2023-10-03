#!/usr/bin/python3
import random


#--------------------------------------------
# range() is an object from <class range> here I pass 5 so it contain 5 values 0 1 2 3 4
# when I list it by list() it convert its object to list object then I print them on screen
# slicing(start, stop, step) >> range(1, 5, 1) > 1 2 3 4 >>start with 1, end before 5, your step is 1
# if I want to reverse start with big value then small that it will not reach then -step you want to pass
# 
#-------------------------------------------------

# print(range(5))
# print(list(range(5)))
# print(list(range(2, 10, 2)))
# print(list(range(8, 1, -2)))
      
# numbers = range(20, 51, 5)
# for numList in numbers:
#     print(numList)

# car = None
# if car:
#     print("car")
# else:
#     print("not car")

#print("Even") if int(input("Enter Integer: ")) % 2 == 0 else print("Odd")

# count = 1
# while count < 90:
#     print(f"[{count}", end = " ")
#     count *= 3
#     print(f"{count}]", end = " ")
#     if count >= 90:
#         print("\n")

# num = random.randint(-10, 10)
# if num > 0:
#     if num % 2 == 0:
#         print(f"{num} is Even")
#     elif num % 2 != 0:
#         print("{:d} is Odd".format(num))
# elif num == 0:
#     print(f"{num} is Zero")
# else:
#     print("{:d} is negative".format(num))


for num in range(0, 21):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
