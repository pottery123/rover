#!usr/bin/emv python
from collections import deque

class Compass(object):
    """
    Provides directional assistance for objects

    initial_direction: [string] initial direction is N E S or W
    """
    def __init__(self,initial_dir):
        self.valid_dirs = ["N","E","S","W"]
        self.initial_dir = initial_dir
        self.deque = deque(self.valid_dirs)
        self.start()

    def start(self):
        self.validate_initial_dir()
        self.find_initial_dir()

    def turn_right(self):
        self.deque.append(self.deque.popleft())

    def turn_left(self):
        self.deque.appendleft(self.deque.pop())

    def current_dir(self):
        return self.deque[0]

    def find_initial_dir(self):
        count = 0
        while self.current_dir() != self.initial_dir:
            count += 1
            self.turn_left()
            if count >= 4:
                Exception('Current direction not found')

    def validate_initial_dir(self):
        if type(self.initial_dir) is not str:
             TypeError("Must be a str")
        elif self.initial_dir not in ["N","W","E","S"]:
              ValueError("Must be str of N E S or W")
