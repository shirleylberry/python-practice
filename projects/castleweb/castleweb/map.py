# castle_map = """
# --------------------
# | A |    TR      B |
# |   |         |    |
# |-  ------------  --
# |         |        |
# |  BR     |    DR  |
# |                  |
# --------     -------
#        |  H  |
# """

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


hallway = Room("Hallway", """You're standing in a hallway that leads inside a castle.
         The hallway is filled with creepy paintings of long dead royalty.
         The rooms ahead are dark except for a dim glow to your right.
         You're not the brightest bulb, so you don't have a torch or any weapons.  Just a cape.
         You've reached the end of the hall.  You can go right or left.""")

bedroom = Room("Bedroom","""The torch you're carrying illuminates an elaborate bedroom, fit for a king.
            There are a few chests of drawers around the room, and some tables.
            You wonder if the treasure could be in here.
            Or maybe even the key?  There is also a door across the way from you.""")

dining_room = Room("Dining Room","""You enter the only room you can see into, which turns out to be a dining room.
        It's illuminated by a torch on the wall.  There's a table in the center, set for dinner.
        All of the place settings are perfect, except for where dead flowers from the centerpiece had fallen.
        The door to the hallway is at your back and there is a torch on the wall to your right.
        You see another door across the room.""")

armory = Room("Armory","""You enter the armory, barely believing your luck.
     I guess it wasn't worth it to haul a sword all the way from town after all!
     You see a sword and a shield hanging on one wall.
     On another is a polearm.  There are daggers scattered about the room as well.""")

barracks = Room("Barracks","""As you enter the barracks you hear a noise that you don't recognize at first.
        As it slowly dawns on you what the noise is, your whole body goes cold.
        Someone is snoring.  Your torch casts light on a bunk where two soldiers sleep.
        As the glow from the torch hits them, they slowly start to wake up.""")



death_scene = Room("Death", "You died.")

treasure_room = Room("Treasure Room", "Congratulations, you got the treasure.")

START = hallway

hallway.add_paths({
    "left" : bedroom,
    "right" : dining_room,
})

bedroom.add_paths({
    "back" : hallway,
    "forward" : armory,
    "door": armory,
})

dining_room.add_paths({
    "back" : hallway,
    "forward" : barracks,
    "door" : barracks,
})

armory.add_paths({
    "back" : bedroom,
    "door" : bedroom,
    "bomb" : death_scene,
})

barracks.add_paths({
    "back" : dining_room,
    "left" : treasure_room,
    "attack" : death_scene,
    "door" : treasure_room,
})
