#!/usr/bin/python3
"""This module houses a class Student"""


class Student:
    """Represent a student object."""

    def __init__(self, first_name, last_name, age):
        """Instatiation of a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of the Student"""
        return self.__dict__
