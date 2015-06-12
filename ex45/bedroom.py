class Bedroom(object):
	def __init__(self, player):
		self.player = player

	castle_map = """
	--------------------
	| A |    TR      B |
	|   |         |    |
	|-  ------------  --
	|         |        |
	|  BR  X  |    DR  |
	|             T    |
	--------     -------
	       |  H  |
	"""
	def __init__(self, player):
		self.player = player


	def enter(self):
		print "You are carrying " + str(self.player.inventory)
		if "key" in self.player.inventory:
			print "You already have the key from this room."
			self.get_next_room()

		if "torch" in self.player.inventory:
			print "The torch you're carrying illuminates an elaborate bedroom, fit for a king."
			print "There are a few chests of drawers around the room, and some tables."
			print "You wonder if the treasure could be in here."
			print "Or maybe even the key?"
			print "There is also a door across the way from you."

	def get_next_room(self):
		if "torch" not in self.player.inventory:
			print "You can't see anything ahead of you."
			print "You trip over your own feet and decide to head back to the hallway."
			return "hallway"

		next_choice = False
		if "key" in self.player.inventory:
			print "You already found the key, so you head to the hallway."
			return "hallway"
		while next_choice != True:
			print "What do you want to do next?"
			choice = raw_input('>')
			if "search" or "key" in choice:
				print "You rifle through the drawers and chests and come up empty handed."
				print "Finally in a fit of rage you throw the pillows off the bed onto the floor."
				print "A key hidden under the pillows is revealed."
				print "You grab it and yell in triumph."
				self.player.inventory.append("key")
				print "You decide to head to the door across the hall."
				next_choice = True
				return "armory"
			elif "door" in choice:
				print "You make a beeline for the door across the hall."
				next_choice = True
				return "armory"
			elif "treasure" in choice:
				print "You rifle through the chests but come up empty handed."
			else:
				print "huh?"
				return "bedroom"


