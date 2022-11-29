#!/usr/bin/python3
for num1 in range(0, 20):
    for num2 in range(num1 + 1, 20):
        if num1 == 18 and num2 == 19:
            print("{}{}".format(num1, num2))
        else:
            print("{}{}".format(num1, num2), end=", ")
