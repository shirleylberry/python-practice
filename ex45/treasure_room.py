class TreasureRoom(object):
	def __init__(self, player):
		self.player = player

	castle_map = """
	--------------------
	| A |    TR      B |
	|   |     X   |    |
	|-  ------------  --
	|         |        |
	|  K      |        |
	|             T    |
	--------     -------
	       |  H  |
	"""

	def enter(self):
		print "You are carrying " + str(self.player.inventory)
		pass
	def get_next_room(self):
		pass