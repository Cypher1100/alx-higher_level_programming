#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listlength = len(my_list)

    newlist = my_list[:]

    if idx >= 0 and idx < listlength:
        newlist[idx] = element

    return (newlist)
