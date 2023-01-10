#!/usr/bin/python3
"""Module for file-appending function."""


def append_write(filename="", text=""):
    """This function appends a string to the
    end of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as mf:
        return mf.write(text)
