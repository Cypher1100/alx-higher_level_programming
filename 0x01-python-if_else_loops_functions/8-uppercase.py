#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(i) >= 97 and ord(i) <= 122:
            ch = chr(ord(ch) - 32)
            print("{}".format(ch), end="")
    print()
