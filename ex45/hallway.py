class Hallway(object):
	def __init__(self, player):
		self.player = player

	hallway_map = """
		--------------------
		| A |    TR      B |
		|   |         |    |
		|-  ------------  --
		|         |        |
		|  K      |        |
		|             T    |
		--------  X  -------
		       |  H  |
		"""
	def enter(self):
		print "You are carrying " + str(self.player.inventory)
		print "You're standing in a hallway that leads inside a castle."
		print "The hallway is filled with creepy paintings of long dead royalty."
		print "The rooms ahead are dark except for a dim glow to your right."
		print "You're not the brighest bulb, so you don't have a torch or any weapons.  Just a cape."
		print "You've reached the end of the hall.  You can go right or left."

	def get_next_room(self):
		print "What next?"
		choice = raw_input(">")
		if "right" in choice:
			return "diningroom"
		elif "left" in choice:
			return "bedroom"
		elif choice == "map":
			print self.hallway_map
			return "hallway"
		elif choice == "inventory":
			if len(self.player.inventory) > 0:
				print self.player.inventory
				return "hallway"
			else:
				print "You aren't carrying anything."
				return "hallway"
		else:
			print "I didn't understand that."
			return "hallway"