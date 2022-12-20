#!/usr/bin/python3
"""Defines a square """


class Square:
    """Represents a square onject"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves the size of square object"""

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
        Calculates the area of the square object
        Returns: The square of the size
        """

        return (self.__size ** 2)

    def my_print(self):
        """
        prints the square value 
        with the character # 
        """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)