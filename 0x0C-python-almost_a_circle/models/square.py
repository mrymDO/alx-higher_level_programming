#!/usr/bin/python3

"""Module models/square.py class Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ a class representing a square which is Subclass of Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiation of square instance
        Args:
            size: size of square
            x(optional): Horizontal coordinate of square's position. Defaults 0
            y(optional): Vertical  coordinate of square's position. Defaults 0
            id(optional): the identifier of the square. Default None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter method size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Sqaure instance.
        Args:
            *args: Variable length argument list containing:
                  id, size, x and y in the given order.
            **Kwargs:Arbitary keyword arguments representing instance attribute
        """
        if len(args) > 0 and args is not None:
            attributes = ['id', 'size', 'x', 'y']
            for i in range(min(len(args), len(attributes))):
                if i == 0 and not isinstance(args[i], int) \
                        and args[i] is not None:
                    raise TypeError("id must be an integer")
                setattr(self, attributes[i], args[i])
        else:
            if "id" in kwargs and not isinstance(kwargs["id"], int) \
                    and kwargs[id] is not None:
                raise TypeError("id must be an integer")
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """ string representation of Square class"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
