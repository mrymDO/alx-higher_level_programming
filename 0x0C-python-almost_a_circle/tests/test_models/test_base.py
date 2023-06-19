#!/usr/bin/python3

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Define test class for Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_initialize_id(self):
        """Create new instances with different values"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        base3 = Base(10)
        self.assertEqual(base3.id, 10)
        base4 = Base(-1)
        self.assertEqual(base4.id, -1)
        base5 = Base(0)
        self.assertEqual(base5.id, 0)
        base6 = Base(798)
        self.assertEqual(base6.id, 798)

    def test_not_int_id(self):
        """Create an instance with non int id"""
        with self.assertRaises(TypeError):
            base7 = Base("not_int")

    def test_type(self):
        """test type"""
        base8 = Base()
        self.assertEqual(type(base8), Base)
        self.assertTrue(isinstance(base8, Base))

    def test_to_json_string(self):
        """test static method JSON string represenation of list_dictionaries"""
        rec1 = Rectangle(10, 7, 2, 8)
        r_dict1 = rec1.to_dictionary()
        json_string1 = Base.to_json_string([r_dict1])
        expect_json1 = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_string1, expect_json1)
        self.assertIsInstance(json_string1, str)
        self.assertIsInstance(r_dict1, dict)

        json_string2 = Base.to_json_string([])
        self.assertEqual(json_string2, '[]')

        json_string3 = Base.to_json_string(None)
        self.assertEqual(json_string3, "[]")

        error = "list_dictionaries must be a list of dictionaries"
        with self.assertRaises(TypeError) as e:
            Base.to_json_string('a')
        self.assertEqual(str(e.exception), error)

        with self.assertRaises(TypeError) as e:
            Base.to_json_string(['a', 'b'])
        self.assertEqual(str(e.exception), error)

        with self.assertRaises(TypeError) as e:
            Base.to_json_string({1: 'a', 2: 'b'})
        self.assertEqual(str(e.exception), error)

        with self.assertRaises(TypeError) as e:
            Base.to_json_string(True)
        self.assertEqual(str(e.exception), error)

        exc2 = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            Base.to_json_string(0, 4)
        self.assertEqual(str(e.exception), exc2)

        with self.assertRaises(TypeError) as e:
            Base.to_json_string((0, 4))
        self.assertEqual(str(e.exception), error)

    def test_save_to_file(self):
        """test class method save_to_file"""
        rec1 = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(2, 4)
        Rectangle.save_to_file([rec1, rec2])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        output = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' +
                  ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(len(f.read()), len(output))

        Rectangle.save_to_file(None)
        output3 = '[]'
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), output3)
        os.remove("Rectangle.json")

        sq1 = Square(5, 2, 3)
        sq2 = Square(4, 1, 0)
        Square.save_to_file([sq1, sq2])
        self.assertTrue(os.path.isfile("Square.json"))
        output2 = ('[{"id": 1, "size": 5, "x": 2, "y": 3},' +
                   ' {"id": 2, "size": 4, "x": 1, "y": 0}]')
        with open("Square.json", 'r') as f:
            self.assertEqual(len(f.read()), len(output2))
        os.remove("Square.json")

        Square.save_to_file([])
        with open("Square.json", 'r') as f:
            self.assertEqual(f.read(), output3)

        with self.assertRaises(AttributeError) as e:
            Base.save_to_file([1, 2])
        self.assertEqual(
                "'int' object has no attribute 'to_dictionary'", str(
                    e.exception))

        with self.assertRaises(TypeError) as e:
            Square.save_to_file(1)
        self.assertEqual("'int' object is not iterable", str(e.exception))

        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file()
        self.assertEqual(
                "save_to_file() missing 1 required positional argument:" +
                " 'list_objs'", str(e.exception))

    def test_from_json_string(self):
        """test method that returns a list from a string representation"""
        list_output1 = Rectangle.from_json_string('')
        self.assertEqual(list_output1, [])

        list_output2 = Rectangle.from_json_string(None)
        self.assertEqual(list_output2, [])

        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        result = [
                {'width': 10, 'height': 4, 'id': 89},
                {'width': 1, 'height': 7, 'id': 7}
        ]
        self.assertCountEqual(list_output, result)
        self.assertEqual(type(list_output), list)

        with self.assertRaises(TypeError) as e:
            list_output = Rectangle.from_json_string(6)
        self.assertEqual(str(e.exception), "json_string must be a string")

        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string()
        self.assertEqual(str(e.exception), "from_json_string() missing 1" +
                         " required positional argument: 'json_string'")

    def test_create(self):
        """test the cerate methods"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        sq1 = Square(2, 4)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual(str(sq1), str(sq2))
        self.assertFalse(sq1 is sq2)
        self.assertFalse(sq1 == sq2)

        with self.assertRaises(TypeError) as e:
            sq3 = "alx"
            sq4 = Rectangle.create(sq3)
            self.assertEqual(
                "create() takes 1 positional argument but 2 were given", str(
                    e.exception))

    def test_load_from_file(self):
        """test method that returns a list of instances"""

        rec1 = Rectangle(3, 5, 1)
        rec2 = Rectangle(2, 4, 0, 0)
        instances = [rec1, rec2]
        Rectangle.save_to_file(instances)
        loaded_instances = Rectangle.load_from_file()
        self.assertEqual(len(loaded_instances), len(instances))
        self.assertNotEqual(loaded_instances[0], instances[0])
        self.assertNotEqual(loaded_instances[1], instances[1])
        self.assertEqual(str(loaded_instances[0]), str(instances[0]))
        self.assertEqual(str(loaded_instances[1]), str(instances[1]))
        os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])

        with self.assertRaises(TypeError) as e:
            list_rectangles_output = Rectangle.load_from_file("alx")
        self.assertEqual(str(e.exception), "load_from_file()" +
                         " takes 1 positional argument but 2 were given")

    def test_save_and_load_csv(self):
        """tests for save and load csv methods"""
        rec1 = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(2, 4)
        list_rectangles_input = [rec1, rec2]

        sq1 = Square(5)
        sq2 = Square(7, 9, 1)
        list_squares_input = [sq1, sq2]

        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()

        self.assertEqual(len(
            list_rectangles_output), len(list_rectangles_input))
        for r_input, r_output in zip(
                list_rectangles_input, list_rectangles_output):
            self.assertEqual(r_input.width, r_output.width)
            self.assertEqual(r_input.height, r_output.height)
            self.assertEqual(r_input.x, r_output.x)
            self.assertEqual(r_input.y, r_output.y)

        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()

        self.assertEqual(len(list_squares_output), len(list_squares_input))
        for s_input, s_output in zip(
                list_squares_input, list_squares_output):
            self.assertEqual(s_input.size, s_output.size)
            self.assertEqual(s_input.x, s_output.x)
            self.assertEqual(s_input.y, s_output.y)

        with self.assertRaises(TypeError) as e:
            list_rectangles_output = Rectangle.load_from_file_csv("alx")
        w = "load_from_file_csv() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), w)


if __name__ == '__main__':
    unittest.main()
