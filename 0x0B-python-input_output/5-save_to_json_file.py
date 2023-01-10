#!/usr/bin/python3
"""Module for JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes an object to a text file using JSON format"""
    with open(filename, "w") as mf:
        json.dump(my_obj, mf)
