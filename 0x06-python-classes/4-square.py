#!/usr/bin/python3
"""A module that defines a square object"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves the size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculates the area of the square
        Returns: The square of size
        """

        return (self.__size ** 2)
