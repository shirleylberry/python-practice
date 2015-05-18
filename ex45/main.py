from sys import exit
import random

from hallway import Hallway
from barracks import Barracks
from armory import Armory
from bedroom import Bedroom
from diningroom import DiningRoom
from treasure_room import TreasureRoom
from death_scene import Death


# this file contains the game engine and the map
# the engine will contain the while loop that actually runs the game and determines end condition
# and will keep track of the user's inventory

# user has an inventory of items
# goal is to make it through a castle to get to treasure
# user must collect a key and a torch before they can get to the treasure
# user must have a sword from the armory to avoid dying in the barracks

# user can find a map if they look for it.  if user has the map in inventory, display ascii map

class Player(object):
	def __init__(self, inventory):
		self.inventory = inventory



class Map(object):
	scenes = {
		"hallway" : Hallway(),
		"barracks" : Barracks(),
		"armory" : Armory(),
		"diningroom" : DiningRoom(),
		"bedroom" : Bedroom(),
		"treasure_room" : TreasureRoom(),
		"death" : Death()
	}

	castle_map = """
	--------------------
	| A |    TR      B |
	|   |         |    |
	|-  ------------  --
	|         |        |
	|  K      |        |
	|             T    |
	--------     -------
	       |  H  |
	"""

	def __init__(self, start_scene, end_scene):
		self.start_scene = start_scene
		self.end_scene = end_scene

	def get_next_scene(self, room_name):
		next = self.scenes.get(room_name)
		return next

	def get_start_scene(self):
		start = self.scenes.get(self.start_scene)
		return start

	def get_end_scene(self):
		end = self.scenes.get(self.end_scene)
		return end





class Engine(object):
	def __init__(self, game_map):
		self.game_map = game_map

	def play(self):
		current_scene = self.game_map.get_start_scene()
		end_scene = self.game_map.get_end_scene()

		while current_scene != end_scene:
			current_scene.enter()
			next_scene_name = current_scene.get_next_room()
			current_scene = self.game_map.get_next_scene(next_scene_name)
		current_scene.enter()


my_map = Map("hallway", "treasure_room")
gm_engine = Engine(my_map)
gm_engine.play()






