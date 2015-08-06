from sys import exit
from map import Room

import random


class Death(Room):
    def __init__(self, player):
        Room.__init__(self, "Death Scene", "You have died.  This is hell.")
        self.player = player

    def enter(self):
        print "You are carrying " + str(self.player.inventory)

    def get_next_room(self):
        print "You're super duper dead."
        exit(1)