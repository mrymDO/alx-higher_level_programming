#!/usr/bin/python3

""" Unittest for  Rectangle class """

import contextlib
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ subclass of TestCase """
    def setUp(self):
        """Reset the nb_objects counter before each test"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """ check for id in Rectangle class"""
        rec1 = Rectangle(5, 12)
        self.assertEqual(rec1.id, 1)
        rec2 = Rectangle(11, 7, 2, 1)
        self.assertEqual(rec2.id, 2)
        rec3 = Rectangle(6, 3, 0, 0, 8)
        self.assertEqual(rec3.id, 8)
        rec4 = Rectangle(16, 7, 5, 4, -2)
        self.assertEqual(rec4.id, -2)

    def test_attributes_values(self):
        """ Create new instances with different values and arguments"""
        rec1 = Rectangle(6, 12, 4, 8, 15)
        self.assertEqual(rec1.width, 6)
        self.assertEqual(rec1.height, 12)
        self.assertEqual(rec1.x, 4)
        self.assertEqual(rec1.y, 8)
        self.assertEqual(rec1.id, 15)

        rec2 = Rectangle(5, 12)
        self.assertEqual(rec2.width, 5)
        self.assertEqual(rec2.height, 12)
        self.assertEqual(rec2.x, 0)
        self.assertEqual(rec2.y, 0)
        self.assertIsNotNone(rec2.id)

    def test_invalid_args(self):
        """ test with invalid arguments """

        with self.assertRaises(TypeError) as e:
            rec1 = Rectangle(9)
        self.assertEqual(
                "__init__() missing 1 required positional argument: 'height'",
                str(e.exception))

        with self.assertRaises(TypeError) as e:
            rec2 = Rectangle()
        self.assertEqual("__init__() missing 2 required positional" +
                         " arguments: 'width' and 'height'", str(e.exception))

        with self.assertRaises(ValueError) as e:
            rec3 = Rectangle(-2, 8, 4, 3, 12)
        self.assertTrue("width must be > 0" in str(e.exception))

        with self.assertRaises(ValueError) as e:
            rec4 = Rectangle(2, -8, 4, 3, 12)
        self.assertTrue("height must be > 0" in str(e.exception))

        with self.assertRaises(TypeError) as e:
            rec5 = Rectangle("alx", 6)
        self.assertEqual("width must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            rec6 = Rectangle(6, "alx")
        self.assertEqual("height must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            rec7 = Rectangle(7, 5, "alx", 3)
        self.assertEqual("x must be an integer", str(e.exception))

        with self.assertRaises(TypeError) as e:
            rec8 = Rectangle(7, 5, 0, "alx")
        self.assertEqual("y must be an integer", str(e.exception))

        with self.assertRaises(ValueError) as e:
            rec8 = Rectangle(7, 5, -3, 4)
        self.assertEqual("x must be >= 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            rec8 = Rectangle(7, 5, 3, -4)
        self.assertEqual("y must be >= 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            rec8 = Rectangle(0, 5, 3, 4)
        self.assertEqual("width must be > 0", str(e.exception))

        with self.assertRaises(ValueError) as e:
            rec8 = Rectangle(7, 0, 3, 4)
        self.assertEqual("height must be > 0", str(e.exception))

    def test_setters(self):
        """ test setters """
        rec = Rectangle(6, 12, 4, 8, 15)
        rec.width = 4
        self.assertEqual(rec.width, 4)
        rec.height = 18
        self.assertEqual(rec.height, 18)
        rec.x = 2
        self.assertEqual(rec.x, 2)
        rec.y = 7
        self.assertEqual(rec.y, 7)

    def test_inheritance(self):
        """ test subclass Rectangle"""
        rec1 = Rectangle(12, 8, 2, 3, 9)
        self.assertTrue(isinstance(rec1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_area_rectangle(self):
        """ test public methode area()"""
        rec1 = Rectangle(3, 2)
        self.assertEqual(rec1.area(), 6)

        rec2 = Rectangle(60, 30, 2, 1, 9)
        self.assertEqual(rec2.area(), 1800)

        with self.assertRaises(TypeError) as e:
            rec3 = Rectangle(3, 2, 2, 1, 12)
            rec3.area("alx")
        self.assertEqual(
                "area() takes 1 positional argument but 2 were given",
                str(e.exception))

    def test_display_rectangle(self):
        """ test public method display with and withou x and y"""
        with self.assertRaises(TypeError) as e:
            rec1 = Rectangle(2, 3)
            rec1.display(8)
        self.assertEqual(
                "display() takes 1 positional argument but 2 were given",
                str(e.exception))

        rec2 = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with contextlib.redirect_stdout(io.StringIO()) as f:
            rec2.display()
        self.assertEqual(f.getvalue(), expected_output)

        rec3 = Rectangle(4, 2, 3, 5)
        expected_output = "\n\n\n\n\n   ####\n   ####\n"
        with contextlib.redirect_stdout(io.StringIO()) as f:
            rec3.display()
        self.assertEqual(f.getvalue(), expected_output)

    def test_str_repre(self):
        """Test for __str__representation"""
        rec1 = Rectangle(3, 2, 1, 1, 9)
        self.assertEqual(str(rec1), "[Rectangle] (9) 1/1 - 3/2")

    def test_update_rectangle_args(self):
        """Test for update method """
        rec1 = Rectangle(5, 5, 5, 5)
        self.assertEqual(str(rec1), "[Rectangle] (1) 5/5 - 5/5")
        rec1.update(12)
        self.assertEqual(str(rec1), "[Rectangle] (12) 5/5 - 5/5")
        rec1.update(12, 8)
        self.assertEqual(str(rec1), "[Rectangle] (12) 5/5 - 8/5")
        rec1.update(12, 8, 4)
        self.assertEqual(str(rec1), "[Rectangle] (12) 5/5 - 8/4")
        rec1.update(12, 8, 4, 1)
        self.assertEqual(str(rec1), "[Rectangle] (12) 1/5 - 8/4")
        rec1.update(12, 8, 4, 1, 2)
        self.assertEqual(str(rec1), "[Rectangle] (12) 1/2 - 8/4")

        with self.assertRaises(TypeError) as e:
            rec1.update("alx")
        self.assertEqual(str(e.exception), "id must be an integer")
        with self.assertRaises(ValueError) as e:
            rec1.update(12, -6, 8)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_update_rectangle_kwargs(self):
        """Test for update method which arguments are *args and **kwargs"""
        rec1 = Rectangle(5, 5, 5, 5)
        self.assertEqual(str(rec1), "[Rectangle] (1) 5/5 - 5/5")
        if rec1.update.__code__.co_argcount > 1:
            return
        rec1.update(width=10)
        self.assertEqual(str(rec1), "[Rectangle] (1) 5/5 - 10/5")
        rec1.update(height=8, y=9, x=8, id=12)
        self.assertEqual(str(rec1), "[Rectangle] (12) 8/9 - 10/8")

        with self.assertRaises(TypeError) as e:
            rec1.update(id="alx")
        self.assertEqual("id must be an integer", str(e.exception))
        with self.assertRaises(ValueError) as e:
            rec1.update(x=12, width=-6, y=8)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_rectangle_to_dictionary(self):
        """test dictionary representation of a Rectangle"""
        rec1 = Rectangle(10, 2, 1, 0)
        rec1_dictionary = rec1.to_dictionary()
        rec_dictionary = {'x': 1, 'y': 0, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(rec1_dictionary, rec_dictionary)
        self.assertEqual(type(rec1_dictionary), dict)
        self.assertEqual(len(rec1_dictionary), len(rec_dictionary))

        rec2 = Rectangle(1, 1)
        rec2_dictionary = {'x': 0, 'y': 0, 'id': 2, 'width': 1, 'height': 1}
        self.assertEqual(rec2.to_dictionary(), rec2_dictionary)
        rec2.update(**rec1_dictionary)
        self.assertEqual(rec2.to_dictionary(), rec_dictionary)
        self.assertFalse(rec1 == rec2)

        with self.assertRaises(TypeError) as e:
            rec3 = Rectangle(10, 2, 1, 0)
            rec3_dictionary = rec3.to_dictionary("alx")
        error = "to_dictionary() takes 1 positional argument but 2 were given"
        self.assertEqual(error, str(e.exception))


if __name__ == '__main__':
    unittest.main()
