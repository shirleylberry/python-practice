from sys import argv

script, input_file = argv


with open(input_file, 'r') as file:
	lines = file.read()
	for line in lines:
		word = lines.split()
		print line
# 		print word
# 	for word in line:
# 		print(word[0])