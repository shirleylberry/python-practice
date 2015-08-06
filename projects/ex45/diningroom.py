class DiningRoom(object):
	def __init__(self, player):
		self.player = player

	castle_map = """
	--------------------
	| A |    TR      B |
	|   |         |    |
	|-  ------------  --
	|         |        |
	|  K      |    X   |
	|             T    |
	--------     -------
	       |  H  |
	"""

	def enter(self):
		print "You are carrying " + str(self.player.inventory)
		print "You enter the only room you can see into, which turns out to be a dining room."
		print "It's illuminated by a torch on the wall.  There's a table in the center, set for dinner."
		print "All of the placesettings are perfect, except for where dead "
		print "flowers from the centerpiece had fallen."
		print "The door to the hallway is at your back and there is a torch on the wall to your right."
		print "You see another door across the room."

	def get_next_room(self):
		next_choice = False
		while next_choice != True:
			print "What do you want to do?"
			choice = raw_input(">")
			if "torch" in choice:
				self.player.inventory.append("torch")
				print "You've picked up a torch."
				print "This should come in handy."
			elif "table" in choice:
				print "You check out the table.  There's nothing of interest here."
			elif "door" in choice:
				print "You head across the room to the door."
				next_choice = True
				return "barracks"
			elif "hallway" in choice:
				print "You head back to the hallway you just came from."
				next_choice = True
				return "hallway"
			else:
				print "I didn't understand that."
				return "diningroom"