#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    lentcounter = 0
    for element in range(x):
        try:
            print(f"{my_list[element]}", end="")
            lentcounter = lentcounter + 1
        except IndexError:
            break
    print()
    return(lentcounter)
