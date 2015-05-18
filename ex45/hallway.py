class Hallway(object):
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
	def enter():
		print "You're standing in a hallway that leads to a castle."
		print "You heard from an old man in a tavern that there's treasure inside."
		print "He gave you a map that lays out the interior of the castle, including the treasure room."
		print "Type inventory at any time to see your inventory, or map to see the map."
		print "Old men generally tend to be trustworthy in these sorts of stories."
		print "The hallway is filled with creepy paintings of long dead royalty."
		print "The rooms ahead are dark except for a dim glow to your right."
		print "You're not the brighest bulb, so you don't have a torch or any weapons."
		print "You've reached the end of the hall.  What do you want to do?"
		self.get_next_room()
	def get_next_room():
		print "What do you want to do?"
		choice = input(">")
		if "right" in choice:
			return ""
		elif choice == "map":
			print self.hallway_map
		elif choice == "inventory":
			print 