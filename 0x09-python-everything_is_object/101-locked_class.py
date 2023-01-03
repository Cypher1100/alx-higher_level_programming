#!/usr/bin/python3
"""This module defines a locked class"""


class LockedClass:
    """
    Allows for the  instatiation of an attribute called first_name only
    """

    __slots__ = ["first_name"]
