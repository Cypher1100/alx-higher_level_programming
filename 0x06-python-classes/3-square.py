#!/usr/bin/python3
"""Defines a square """


class Square:
    """Represents a square object"""

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Methot calculates the area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)
