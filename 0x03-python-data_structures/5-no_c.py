#!/usr/bin/python3
def no_c(my_string):
    newstring = my_string.translate({ord(alphabet): None for alphabet in 'cC'})
    return (newstring)
