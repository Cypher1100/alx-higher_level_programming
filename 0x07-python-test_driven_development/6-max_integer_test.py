#!/usr/bin/python3
"""
This module houses a function that finds the max integer in a list
"""


def max_integer(list=[]):
    """This function is used to find the maximum integer in a list of integers
    If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    max_int = list[0]
    count = 1
    while count < len(list):
        if list[count] > max_int:
            max_int == list[count]
        count = count + 1
    return max_int
