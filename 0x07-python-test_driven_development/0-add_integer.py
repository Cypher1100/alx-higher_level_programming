#!/usr/bin/python3
"""This module houses a functuon that sums two imtegers, floats are casted to integers"""

def add_integer(a, b=98):
    """
    The function takes 2 integers or floats and return the sum.
    Arguments must be integers or floats, else a TypeError is raised with an error message.
    """
    if (not isinstance(int, a) and not isinstance(float, a)):
        raise TypeError("a must be an integer")
    if (not isinstance(int, b) and not isinstance(float, b)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
