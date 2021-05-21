#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    unittest class for max_integer
    """
    def test_module_doc(self):
        """Tests module docstring"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_doc(self):
        """Tests function docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """Tests for empty list"""
        l = []
        self.assertIsNone(max_integer(l))

    def test_one_element_list(self):
        """Tests for a one element in the list"""
        l = [66]
        self.assertEqual(max_integer(l), 66)

    def test_max_middle(self):
        """Tests for maximum in the middle"""
        l = [1, 66, 9]
        self.assertEqual(max_integer(l), 66)

    def test_max_end(self):
        """Tests for maximum in the end"""
        l = [1, 6, 9]
        self.assertEqual(max_integer(l), 9)

    def test_max_begin(self):
        """Tests for maximum in the begin"""
        l = [66, 9, 1]
        self.assertEqual(max_integer(l), 66)

    def test_negative_numbers(self):
        """Tests for a negative number"""
        l = [-2, -6, -4]
        self.assertEqual(max_integer(l), -2)

    def test_one_negative_number(self):
        """Tests for a negative number"""
        l = [-2, 0, 1]
        self.assertEqual(max_integer(l), 1)

if __name__ == "__main__":
    unittest.main()
