#!/usr/bin/python3
"""Module JSON-to-object function"""


import json


def from_json_string(my_str):
    """This function returns the Python object
    representation of a JSON string
    """
    return json.loads(my_str)
