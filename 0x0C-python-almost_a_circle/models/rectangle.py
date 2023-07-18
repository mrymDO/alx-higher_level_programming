#!/usr/bin/python3
""" Module rectangle.py is a class Rectangle that inherits """

from models.base import Base


class Rectangle(Base):
    """
    Subclass of Base class representing a rectangle.
    Attributes:
           id: identified for rectangle.
           width: width of rectangle.
           height: height of rectangle.
           x: horizontal coordinate for rectangle's position
           y: vertical coordinate for rectangle's position
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes Rectangle instance """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for the width attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x attribute """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y attribute """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """ Prints Rectangle instance with the character # """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ override the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle
        Args:
            *args: Variable_length arguments representing
            the attributes of the rectangle in the following order:
              - 1st arguement: id attribute
              - 2nd argument: width attribute
              - 3rd argument: height attribute
              - 4th argument: x attribute
              - 5th argument: y attribute
              **kwargs: keyword arguments representing attributes
                        of the rectangle as key/value pairs
                        the order of keyword arguments is not important
            If *args exists, **kwargs will be skipped
        """
        if len(args) > 0 and args is not None:
            if len(args) > 0:
                if not isinstance(args[0], int) and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    if not isinstance(value, int) and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ Returns the dictionary  representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }
