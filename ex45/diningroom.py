class DiningRoom(object):

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

	def enter():
		print "You enter the only room you can see into, which turns out to be a dining room."
		print "There's a table in the center, set for dinner."
		print "All of the placesettings are perfect, except for where dead "
		print "flowers from the centerpiece had fallen."
		print "The door to the hallway is at your back and there is a torch on the wall to your right."
		print "You see another door across the room."

	def get_next_room():
		print "What do you want to do?"
		choice = input(">")