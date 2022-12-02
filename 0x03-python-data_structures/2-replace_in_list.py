#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    listlength = len(my_list)
    element = my_list[idx]
    if idx < 0:
        return my_list
    elif idx > (listlength -1):
        return my_list
    else:
        return my_list


