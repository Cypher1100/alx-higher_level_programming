#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_key_list = list(a_dictionary.keys())
    dict_key_list.sort()
    for key in dict_key_list:
        print(f"{} : {}".format(key, a_dictionary.get(key))
