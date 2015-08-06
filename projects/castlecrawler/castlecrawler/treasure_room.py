from map import Room

class TreasureRoom(Room):
    def __init__(self, player):
        Room.__init__(self, "Treasure Room", "The castle's treasure room.  There's a chest"
                                             "in the corner of the room.")
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

    def get_next_room(self):
        if "key" in self.player.inventory:
            print "Congratulations, you won!"