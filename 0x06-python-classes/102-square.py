#!/usr/bin/python3
"""My square object module"""


class Square:
    """defines a square object"""

    def __init__(self, size=0):
        """Create a Square
        Args: size which is the length of one side of a Square
        """
        self.__size = size

    @property
    def size(self):
        """"The propery of size as the len of a side of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Get the area of a Square
        Returns: The square of size
        """
        return self.__size * self.__size

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
