import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'rover')))

from rover import Rover
from compass import Compass

class TestRover(unittest.TestCase):
    def test_rover_has_correct_initial_directions(self):
        r = Rover("R")
        self.assertEqual(r.initial_dir,"R")
    def test_rover_has_correct_coordinates(self):
        r = Rover("W", [0,3])
        self.assertEqual(r.cart,[0,3])
    def test_rover_has_correct_default_coordinates(self):
        r = Rover("S")
        self.assertEqual(r.cart, [0,0])
