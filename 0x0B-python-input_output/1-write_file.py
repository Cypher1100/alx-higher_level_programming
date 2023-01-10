#!/usr/bin/python3
"""Module for a file-writing function."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file
    """
    with open(filename, "w", encoding="utf-8") as mf:
        return mf.write(text)
