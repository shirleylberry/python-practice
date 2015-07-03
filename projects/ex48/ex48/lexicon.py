

def get_type(word):
	word_types = {
		"direction" : ["north", "south", "east", "west", "up", "left", "back", "right"],
		"verb" : ["go", "stop", "kill", "eat"],
		"filler" : ["the", "in", "of", "from", "at", "it", "and"],
		"noun" : ["door", "bear", "princess", "cabinet"],
	}

	for keys, values in word_types.iteritems():
		if word.lower() in values:
			return (keys, word)
		elif word.isdigit():
			return ('number', int(word))
	# if it isn't in allowed word list tell user error
	return ('error', word)

def scan(string):
	word_list = string.split()
	sentence = []
	for word in word_list:
		word_tup = get_type(word)
		sentence.append(word_tup)
	# print sentence
	return sentence

scan("north of my door")