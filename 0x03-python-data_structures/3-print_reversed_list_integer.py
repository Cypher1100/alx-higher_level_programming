#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    listlength = len(my_list)
    my_list.reverse()
    for nums in range(listlength):
        print("{:d}".format(my_list[nums]))
