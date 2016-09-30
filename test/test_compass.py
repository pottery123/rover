# import os
# import sys
import unittest
#
# sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'rover')))

from .context import Rover
from .context import Compass

class TestCompass(unittest.TestCase):
    def test_turn_right(self):
        c = Compass("N")
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

    #
    # def test_valid_location(self):
    #     c = Compass("X")
    #     self.assertRaises(ValueError, c.initial_direction)
