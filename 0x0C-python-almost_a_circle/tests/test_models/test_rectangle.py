#!/usr/bin/python3
"""
Contains test for Rectangle class
"""

import unittest
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangleDocs(unittest.TestCase):
    """Test module docstring"""
    def test_module_docstring(self):
        """Tests for the presence of a module docstring"""
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Test class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)
