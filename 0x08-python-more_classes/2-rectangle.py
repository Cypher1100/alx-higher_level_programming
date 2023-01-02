#!/usr/bin/python3
"""This class defines a rectangle"""


class Rectangle:
    """Represents a rectangle object"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        width must be an integer, otherwise raise a TypeError exception with
        the message width must be an integer
        if width is less than 0, raise a ValueError exception with the message
        width must be >= 0

        height must be an integer, otherwise raise a TypeError exception with
        the message height must be an integer
        if height is less than 0, raise a ValueError exception with the message 
        height must be >= 0

        if width or height is equal to 0, perimeter is equal to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
