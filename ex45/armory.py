class Armory(object):

	castle_map = """
	--------------------
	| A |    TR      B |
	| X |         |    |
	|-  ------------  --
	|         |        |
	|  K      |        |
	|             T    |
	--------     -------
	       |  H  |
	"""

	def enter():
		print "You enter the armory, barely believing your luck."
		print "I guess it wasn't worth it to haul a sword all the way from town."
		print "You see a sword and a shield hanging on one wall."
		print "On another is a polearm."
		print "There are daggers scattered about the room as well."
		self.get_next_room()
	def get_next_room():
		print "What do you want to do?"
		choice = input(">")