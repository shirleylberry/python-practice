from castlecrawler.map import Room


class Armory(Room):
    def __init__(self, player):
        Room.__init__(self, "Armory", "The castle's Armory.  It's full of weapons, "
                                "as armories usually are.")
        self.player = player


castle_map = """
	--------------------
	| A |    TR      B |
	| X |         |    |
	|-  ------------  --
	|         |        |
	|  BR     |   DR   |
	|             t    |
	--------     -------
	       |  H  |
	"""


def enter(self):
    print "You are carrying " + str(self.player.inventory)
    print "You enter the armory, barely believing your luck."
    print "I guess it wasn't worth it to haul a sword all the way from town after all!"
    print "You see a sword and a shield hanging on one wall."
    print "On another is a polearm."
    print "There are daggers scattered about the room as well."


def get_next_room(self):
    print "What do you want to do?"
    choice = raw_input(">")
    if "dagger" in choice:
        print "You grab a pair of daggers and tuck them into your belt."
        self.player.inventory.append("daggers")
        print "You then head back to the bedroom."
        return "bedroom"

    elif "sword" in choice or "shield" in choice:
        print "You grab the sword and shield off the wall."
        self.player.inventory.append("sword")
        self.player.inventory.append("shield")
        print "You then head back to the bedroom."
        return "bedroom"

    elif "polearm" in choice:
        print "You grab the polearm off the wall."
        print "Bold choice.  Do you even know what a polearm is?"
        self.player.inventory.append("polearm")
        print "You then head back to the bedroom."
        return "bedroom"
    else:
        print "huh?"
        return "armory"

