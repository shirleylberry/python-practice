from sys import exit
import random

from hallway import Hallway
from barracks import Barracks
from armory import Armory
from bedroom import Bedroom
from diningroom import DiningRoom
from treasure_room import TreasureRoom
from death_scene import Death

from map import Room

# this file contains the game engine and the map
# the engine will contain the while loop that actually runs the game and determines end condition
# and will keep track of the user's inventory

# user has an inventory of items
# goal is to make it through a castle to get to treasure
# user must collect a key and a torch before they can get to the treasure
# user must have a sword from the armory to avoid dying in the barracks

# user can find a map if they look for it.  if user has the map in inventory, display ascii map
#
# class Player(object):
# 	def __init__(self, name, inventory):
# 		self.name = name
# 		self.inventory = inventory
#
#
# class Map(object):
# 	def __init__(self, start_scene, end_scene, player):
# 		self.start_scene = start_scene
# 		self.end_scene = end_scene
# 		self.player = player
#
# 	def get_scene(self, player, string):
# 		scenes = {
# 			"hallway" : Hallway(player),
# 			"barracks" : Barracks(player),
# 			"armory" : Armory(player),
# 			"diningroom" : DiningRoom(player),
# 			"bedroom" : Bedroom(player),
# 			"treasure_room" : TreasureRoom(player),
# 			"death_scene" : Death(player)
# 		}
# 		# try:
# 		return scenes.get(string)
# 		# except:
# 		print "That scene doesn't exist."
# 			# exit()
#
# 	castle_map = """
# 	--------------------
# 	| A |    TR      B |
# 	|   |         |    |
# 	|-  ------------  --
# 	|         |        |
# 	|  K      |        |
# 	|             T    |
# 	--------     -------
# 	       |  H  |
# 	"""
#
#
# 	def get_next_scene(self, room_name):
# 		next = self.get_scene(player, room_name)
# 		return next
#
# 	def get_start_scene(self):
# 		start = self.get_scene(player, self.start_scene)
# 		return start
#
# 	def get_end_scene(self):
# 		end = self.get_scene(player, self.end_scene)
# 		return end
#
#
#
#
#
# class Engine(object):
# 	def __init__(self, game_map, player):
# 		self.game_map = game_map
# 		self.player = player
#
# 	def play(self):
# 		current_scene = self.game_map.get_start_scene()
# 		end_scene = self.game_map.get_end_scene()
#
# 		while current_scene != end_scene:
# 			current_scene.enter()
# 			next_scene_name = current_scene.get_next_room()
# 			current_scene = self.game_map.get_next_scene(next_scene_name)
# 		current_scene.enter()
#
#
# print "Enter your name."
# name = raw_input("> ")
# inventory = []
# player = Player(name, inventory)
#
# print "Greetings %s" %player.name
# print "You find yourself standing at the start of a winding road leading to a castle."
# print "You heard from an old man in a tavern that there's treasure inside."
# print "He gave you a map that lays out the interior of the castle, including the treasure room."
# print "Type inventory at any time to see your inventory, or map to see the map."
# print "Old men generally tend to be trustworthy in these sorts of stories."
# print "You decide to walk up the road.  As you approach the castle"
# print "the doors swing open on their own.  Not creepy at all..."
# print "You hesitantly walk inside."
#
# my_map = Map("hallway", "treasure_room", player)
# gm_engine = Engine(my_map, player)
# gm_engine.play()
#
#
#
#
#
#
