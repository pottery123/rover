import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'rover')))

from rover import Rover
from compass import Compass

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
        c = Compass("E").find_initial_dir()
        c.turn_left()
        self.assertEqual('N', c.current_dir())

    def test_current_dir(self):
        c = Compass("E").find_initial_dir()
        self.assertEqual('E', c.current_dir())
