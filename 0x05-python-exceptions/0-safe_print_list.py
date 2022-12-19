#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    totalent = 0
    for element in range(x):
        try:
            print(f"{my_list[element]}", end="")
            totalen = totalen + 1
        except IndexError:
            break
    print()
    return(totalen)
