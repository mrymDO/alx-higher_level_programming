#!/usr/bin/python3
"""
Module that defines a rectangle
"""


class Rectangle:
    """
    a class Rectangle that defines a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with specified width and height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """returns a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return""
        rect_str = ""
        for _ in range(self.__height):
            rect_str += str(self.print_symbol) * self.__width + "\n"
        return rect_str.rstrip()

    def __repr__(self):
        """
        returns a string representation of rectangle,
        able to recreate a new instance using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Delete an instance of rectangle class
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """getter methode to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method to set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method to retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method to set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to compare 2 rectangles."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Class method that returns a new Rectangle instance,
        with widtth == height == size.
        """
        return cls(size, size)
