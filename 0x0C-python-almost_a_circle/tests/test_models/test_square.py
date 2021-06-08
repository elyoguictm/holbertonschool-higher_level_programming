"""
Contains tests for Square class
"""

import unittest
from models import square
from models.base import Base
Square = square.Square


class TestSquare(unittest.TestCase):
    """Test suit for Square class"""
    def test_module_docstring(self):
        """Test module docstring"""
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_docstring(self):
        """Test Square class docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)
