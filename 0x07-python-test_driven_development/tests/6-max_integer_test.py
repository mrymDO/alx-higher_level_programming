#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_list(self):
        """Test with regular numbers"""
        list1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(list1), 4)

    def test_one_element(self):
        """test with a list of one element"""
        list2 = [9]
        self.assertEqual(max_integer(list2), 9)

    def test_empty(self):
        """test with an empty list"""
        list3 = []
        self.assertIsNone(max_integer(list3))

    def test_negative_num(self):
        """test with negative number"""
        list4 = [-1, -2, -3, -4]
        self.assertEqual(max_integer(list4), -1)

    def test_pos_nega_num(self):
        """test with negative and positive numbers"""
        list5 = [-1, -2, 3, 4]
        self.assertEqual(max_integer(list5), 4)

    def test_float_num(self):
        """test with float numbers"""
        list6 = [1.1, 2.1, 3.1, 4.9]
        self.assertEqual(max_integer(list6), 4.9)

    def test_duplicate_numbers(self):
        """test with duplicated numbers"""
        list7 = [7, 7, 7, 9, 6, 9, 6]
        self.assertEqual(max_integer(list7), 9)

    def test_oneele_multime(self):
        """test with a unique number duplicated"""
        list8 = [1, 1, 1, 1]
        self.assertEqual(max_integer(list8), 1)

    def test_non_int(self):
        """test with strings"""
        list9 = ["a", "b", "c", "d"]
        self.assertEqual(max_integer(list9), "d")

    def test_int_string(self):
        """test with a lits of strings and integers"""
        list10 = [1, 2, 3, "a"]
        self.assertRaises(TypeError, max_integer, list10)

    def test_notlist(self):
        """test type list"""
        list11 = 55
        self.assertRaises(TypeError, max_integer, list11)

    def test_nonelist(self):
        """test <none list"""
        list12 = None
        self.assertRaises(TypeError, max_integer, list12)


if __name__ == '__main__':
    unittest.main()
