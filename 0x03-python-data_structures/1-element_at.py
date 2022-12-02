#!/usr/bin/python3

def element_at(my_list, idx):
    listlength = len(my_list)
    if idx < 0:
        return None
    elif idx > listlength:
        return None
    else:
        return (my_list[idx])
#e
