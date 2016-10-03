# -*- coding: utf-8 -*-

import unittest
from rover import Compass

class TestCompass(unittest.TestCase):
    def test_compass_has_correct_initial_directions(self):
        with self.assertRaises(ValueError):
            Compass('R')

    def test_turn_right(self):
        c = Compass('N')
        c.turn_left()
        self.assertEqual('W', c.current_dir())

    def test_turn_left(self):
        c = Compass("N")
        c.turn_right()
        self.assertEqual('E', c.current_dir())

    def test_turn_left_twice(self):
        c = Compass("E")
        c.turn_left()
        self.assertEqual('N', c.current_dir())

    def test_current_dir(self):
        c = Compass("E")
        self.assertEqual('E', c.current_dir())

<<<<<<< HEAD

    def test_valid_location(self):
         c = Compass("X")
         self.assertRaises(ValueError, c.initial_direction)
=======
>>>>>>> 2e72e7567eefb2c2333cc749a9df13e93e9ef01a
