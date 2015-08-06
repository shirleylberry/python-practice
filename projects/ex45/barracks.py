class Barracks(object):

	def __init__(self, player):
		self.player = player

	castle_map = """
	--------------------
	| A |    TR      B |
	|   |         |  X |
	|-  ------------  --
	|         |        |
	|  K      |        |
	|             T    |
	--------     -------
	       |  H  |
	"""

	def enter(self):
		print "You are carrying " + str(self.player.inventory)
		if "torch" in self.player.inventory:
			print "As you enter the barracks you hear a noise that you don't recognize at first."
			print "As it slowly dawns on you what the noise is, your whole body goes cold."
			print "Someone is snoring."
			print "Your torch casts light on a bunk where two soldiers sleep."
			print "As the glow from the torch hits them, they slowly start to wake up."			

	def get_next_room(self):
		if "torch" not in self.player.inventory:
			print "You realize you can't see jack shit in the next room."
			print "You retreat back into the dining room."
			return "diningroom"

		if "sword" in self.player.inventory:
			print "Holy shit good thing you grabbed that sword and shield."
			print "You pull your sword out and hold it in front of your face."
			print "Yeah... that's probably how you use that..."
			print "You block the first soldier's attack with your shield and stick your sword through his gut."
			print "The second solder comes at you from the side and you duck."
			print "You're pretty good at this!"
			print "You spin around and cut him in half holy shit."
			print "You continue on into the next room."
			return "treasure_room"
		elif "daggers" in self.player.inventory:
			print "Holy shit good thing you grabbed those daggers."
			print "You throw your first dagger at the soldier and manage to get him right between the eyes."
			print "The second solder comes at you from the side and you duck."
			print "You're pretty good at this!"
			print "You spin around and slash him across the guts.  He falls dead."
			print "You continue on into the next room."
			return "treasure_room"
		elif "polearm" in self.player.inventory:
			print "Holy shit good thing you grabbed this polearm."
			print "You bring your polearm up in front of you.  It's... unwieldy but it'll do."
			print "You thrust forward and catch the first soldier in the stomach."
			print "You're pretty good at this!"
			print "The second soldier comes at you before you can pull your polearm out."
			print "You duck down and dodge him, pulling your polearm out as you spin."
			print "You keep spinning and slash him across the chest.  He falls dead."
			print "You continue on into the next room."
			return "treasure_room"
		else:
			print "Well... you have no weapon.  And they do..."
			print "You're kind of fucked."
			return "death_scene"






