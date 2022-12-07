#!/usr/bin/python3
def number_keys(a_dictionary):
    key_list = tuple(a_dictionary.keys())
    counter = 0

    for key in key_list:
        counter += 1
    return counter
