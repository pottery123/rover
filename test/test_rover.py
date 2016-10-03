# -*- coding: utf-8 -*-

import unittest
from rover import Rover

class TestRover(unittest.TestCase):
    def test_rover_has_correct_coordinates(self):
        r = Rover("W", [0,3])
        self.assertEqual(r.cart,[0,3])
    def test_rover_has_correct_default_coordinates(self):
        r = Rover("S")
        self.assertEqual(r.cart, [0,0])
