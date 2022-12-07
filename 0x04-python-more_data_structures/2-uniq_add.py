#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_uniqlist = set(my_list)
    counter = 0

    for num in add_uniqlist:
        counter = counter + num

    return counter
