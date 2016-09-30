#!usr/bin/emv python
from collections import deque

class Compass(object):
    """
    Provides directional assistance for objects

    initial_direction: [string] initial direction is N E S or W
    """
    def __init__(self,initial_direction):
        self.valid_directions = ["N","E","S","W"]
        self.validate_initial_dir(initial_direction)
        self.initial_direction = initial_direction
        self.deque = deque(self.valid_directions)
        self.find_initial_dir()

    def turn_right(self):
        self.deque.append(self.deque.popleft())

    def turn_left(self):
        self.deque.appendleft(self.deque.pop())

    def current_dir(self):
        return self.deque[0]


    def find_initial_dir(self):
        while self.current_dir() != self.initial_direction:
            self.turn_left()

    def validate_initial_dir(self,initial_direction):
        if type(initial_direction) != str:
             TypeError("Must be a str")
        elif initial_direction not in ["N","W","E","S"]:
             ValueError("Must be str of N E S or W")
