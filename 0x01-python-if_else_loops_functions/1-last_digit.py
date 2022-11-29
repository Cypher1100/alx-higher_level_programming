#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mynum = abs(number) % 10
if number < 0:
    mynum = -mynum
print(f"Last digit of {number:d} is {mynum:d}", end=" ")
if mynum > 5:
    print(f"and is greater than 5")
elif mynum == 0:
    print(f"and is 0")
elif mynum < 6 and not 0:
    print(f"and is less than 6 and not 0")
