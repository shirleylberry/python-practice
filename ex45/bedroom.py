class Bedroom(object):

	castle_map = """
	--------------------
	| A |    TR      B |
	|   |         |    |
	|-  ------------  --
	|         |        |
	|  K   X  |        |
	|             T    |
	--------     -------
	       |  H  |
	"""

	def enter():
		if "torch" in inventory:
			print "The torch you're carrying illuminates an elaborate bedroom, fit for a king."
			print "There are a few chests of drawers around the room, and some tables."
			print "You wonder if the treasure could be in here."

		else:
			print "You can't see anything ahead of you."
			print "You trip over your own feet and decide to head back to the hallway."
			return "hallway"
	def get_next_room():
		pass