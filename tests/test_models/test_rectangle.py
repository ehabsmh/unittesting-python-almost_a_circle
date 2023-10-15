#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle

"""
Test module for Rectangle class
"""


class TestRectangle(unittest.TestCase):

    def test_width_height(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        r1.width = 12
        r1.height = 4
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 4)

    def test_default_params(self):
        r1 = Rectangle(10, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_default_id(self):
        r1 = Rectangle(21, 7)
        r1 = Rectangle(15, 3)
        r2 = Rectangle(10, 3)
        self.assertEqual(r2.id, r1.id + 1)

    def test_with_args(self):
        r1 = Rectangle(10, 2, 4, 4)


    def test_id(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)

    def test_args(self):
        pass

    def test_types(self):
        pass

    def test_private_att(self):
        pass
