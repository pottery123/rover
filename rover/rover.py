#!usr/bin/emv python
import compass

class Rover(object):
    def __init__(self,initial_dir,cart=[0,0]):
        self.cart = cart
        self.initial_dir = initial_dir
        self.compass = compass.Compass(self.initial_dir)

    def move(self):
        if self.compass.current_dir()   == "N":
            self.move_north()
        elif self.compass.current_dir() == "W":
            self.move_west()
        elif self.compass.current_dir() == "E":
            self.move_east()
        elif self.compass.current_dir() == "S":
            self.move_south()

    def turn_left(self):
        self.compass.turn_left()

    def turn_right(self):
        self.compass.turn_right()

    def move_north(self):
        self.cart[1] += 1

    def move_east(self):
        self.cart[0] += 1

    def move_south(self):
        self.cart[1] -= 1

    def move_west(self):
        self.cart[0] -=1
