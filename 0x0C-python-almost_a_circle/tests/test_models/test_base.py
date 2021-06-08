#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest
from models import base
Base = base.Base


class TestBase(unittest.TestCase):
    """Test suit for Base class"""
    def test_module_docstring(self):
        """Test module docstring"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstring(self):
        """Test Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)
