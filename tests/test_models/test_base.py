#!/usr/bin/python3

"""
Testing base module
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Defines tests for Base class"""

    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_with_args(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base(25)
        self.assertEqual(b2.id, 25)
        self.assertNotEqual(b1.id, b2.id)

    def test_none_arg(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_instantiation(self):
        b1 = Base()
        self.assertIsInstance(b1, Base)
        b2 = Base(12)
        self.assertIsInstance(b2, Base)

    def test_public_att(self):
        b1 = Base(18)
        b1.id = 20
        self.assertNotEqual(b1.id, 18)

    def test_hidden_att(self):
        b1 = Base()
        with self.assertRaises(AttributeError):
            self.assertEqual(b1.__nb_objects, 1)
            self.assertEqual(b1.nb_objects, 1)
