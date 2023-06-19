#!/usr/bin/python3

"""
Module test_square
test cases for square class
"""
import io
import contextlib
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """ Test class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):
        """ test for square attributes """
        sq1 = Square(5)
        self.assertEqual(sq1.id, 1)
        self.assertEqual(sq1.width, 5)
        self.assertEqual(sq1.height, 5)
        sq2 = Square(3, 1, 3)
        self.assertEqual(sq2.width, 3)
        self.assertEqual(sq2.x, 1)
        self.assertEqual(sq2.y, 3)
        self.assertEqual(sq2.id, 2)

        with self.assertRaises(TypeError) as e:
            sq3 = Square()
        self.assertEqual(
                "__init__() missing 1 required positional argument: 'size'",
                str(e.exception))

    def test_str(self):
        """Test __str__ representation"""
        sq1 = Square(8, 2, 1, 12)
        self.assertEqual(str(sq1), "[Square] (12) 2/1 - 8")

    def test_square_inheritence(self):
        """ check square inheritence """
        square = Square(5, 2, 3, 10)
        self.assertIsInstance(square, Square)
        self.assertIsInstance(square, Rectangle)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    def test_square_area(self):
        """test area method"""
        sq = Square(5)
        self.assertEqual(sq.area(), 25)

    def test_square_update(self):
        """test update method"""
        sq = Square(5)
        sq.update(10)
        self.assertEqual(str(sq), "[Square] (10) 0/0 - 5")
        sq2 = Square(10, 12, 2, 1)
        self.assertEqual(str(sq2), "[Square] (1) 12/2 - 10")

    def test_square_display(self):
        """test display method"""
        sq = Square(3)
        expected_output = "###\n###\n###\n"
        with contextlib.redirect_stdout(io.StringIO()) as f:
            sq.display()
        self.assertEqual(f.getvalue(), expected_output)

    def test_square_setter(self):
        """test setter size"""
        sq1 = Square(5)
        self.assertEqual(sq1.size, 5)
        sq3 = Square(5, 6, 3, 1)
        self.assertEqual(sq3.size, 5)

        with self.assertRaises(TypeError) as e:
            sq2 = Square("9")
        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            sq4 = Square(8, "9")
        self.assertEqual(str(e.exception), "x must be an integer")
        with self.assertRaises(TypeError) as e:
            sq5 = Square(8, 7, "9")
        self.assertEqual(str(e.exception), "y must be an integer")
        with self.assertRaises(ValueError) as e:
            sq6 = Square(-5, 3, 1)
        self.assertEqual(str(e.exception), "width must be > 0")
        with self.assertRaises(ValueError) as e:
            sq6 = Square(5, -3, 1)
        self.assertEqual(str(e.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as e:
            sq6 = Square(5, 3, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")
        with self.assertRaises(ValueError) as e:
            sq6 = Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_square_update(self):
        """test update method"""

        sq1 = Square(5, 4, 3, 2)
        sq1.update(10, 8, 6)
        self.assertEqual(sq1.id, 10)
        self.assertEqual(sq1.size, 8)
        self.assertEqual(sq1.x, 6)
        sq1.update(y=9)
        self.assertEqual(sq1.y, 9)
        sq1.update(x=0, id=12, size=13)
        self.assertEqual(sq1.x, 0)
        self.assertEqual(sq1.id, 12)
        self.assertEqual(sq1.size, 13)
        sq1.update()
        self.assertEqual(sq1.x, 0)
        self.assertEqual(sq1.id, 12)
        self.assertEqual(sq1.size, 13)

        sq2 = Square(5)
        with self.assertRaises(TypeError) as e:
            sq2.update("alx", 8, 2, 1)
        self.assertEqual(str(e.exception), "id must be an integer")
        with self.assertRaises(ValueError) as e:
            sq2.update(12, -8, 2, 1)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_square_to_dictionary(self):
        """test to_dictionary method"""
        sq1 = Square(10, 2, 1)
        sq1_dictionary = sq1.to_dictionary()
        sq1_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(sq1_dictionary, sq1_dict)
        self.assertEqual(len(sq1_dictionary), len(sq1_dict))
        self.assertEqual(type(sq1_dictionary), dict)
        sq2 = Square(1, 1)
        self.assertEqual(str(sq2), "[Square] (2) 1/0 - 1")
        sq2.update(**sq1_dictionary)
        self.assertEqual(sq2.to_dictionary(), sq1_dict)
        self.assertEqual(str(sq2), "[Square] (1) 2/1 - 10")
        self.assertFalse(sq1 == sq2)

        with self.assertRaises(TypeError) as e:
            sq3 = Square(10, 2, 1, 12)
            sq3_dictionary = sq3.to_dictionary("alx")
        error = "to_dictionary() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), error)


if __name__ == '__main__':
    unittest.main()
