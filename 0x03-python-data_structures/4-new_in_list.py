#!/usr/bin/python3
def new_in_list(my_list, idx, element):
       new_list = my_list[:]
       listlength = len(my_list)

       if idx < 0:
           return (my_list)
       elif idx > (listlength - 1):
           return (my_list)
       elif idx >= 0 and idx < listlength:
           new_list[idx] = element

       return (new_list)
