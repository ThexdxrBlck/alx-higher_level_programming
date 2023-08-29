#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __int__(self, size=0):
        """Initalize a new square.

        Agrs:
        size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer.")
        elif size < 0:
            raise ValueError("size must be an integer")
        self.__size = size

        def area(self):
            """Return the current area of the square."""
            return (self.__size * self.__size)
