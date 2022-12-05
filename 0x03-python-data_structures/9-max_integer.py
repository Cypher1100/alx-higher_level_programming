#!/usr/bin/python3
def max_integer(my_list=[]):
    listlength = len(my_list)

    if listlength == 0:
        return (None)

    max_integer = my_list[0]

    for num in range(1, listlength):
        if my_list[num] > max_integer:
            max_integer = my_list[num]

    return (max_integer)
