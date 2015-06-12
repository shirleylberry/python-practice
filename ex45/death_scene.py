from sys import exit
import random

class Death(object):
	def __init__(self, player):
		self.player = player

	def enter(self):
		print "You are carrying " + str(self.player.inventory)
		
	def get_next_room(self):
		print "You're super duper dead."
		exit(1)