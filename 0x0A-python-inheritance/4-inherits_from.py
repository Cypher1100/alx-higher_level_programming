#!/usr/bin/python3
"""This modulechecks if object is an instance of a 
class that inherited from the specified class or not"""


def inherits_from(obj, a_class):
    """This function eturns true if object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
