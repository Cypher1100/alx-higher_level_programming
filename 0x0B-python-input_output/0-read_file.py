#!/usr/bin/python3
"""This module defines a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """This function Prints the contents of a UTF8 text file"""
    with open(filename, encoding= "utf-8") as myfile:
        print(myfile.read(), end="")
