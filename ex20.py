from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

# this seek command tells the program to go to 0 spaces offset from
# the start of the file; you can specify an optional command to tell 
# it where to seek from, but 0 (the start) is the default and applies here
def rewind(f):
	f.seek(0)

# reads a single line
#The file f is responsible for maintaining the current position in the file 
# after each readline() call, so that it will keep reading each line.

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1

# readline() is called in each print_a_line function; readline reads the current
# line and then the current line goes to the next line
print_a_line(current_line, current_file)

# ALL that this variable does is enable us to label each line; it doesn't
# actually do anything to define what the current line is; the function call
# already preserves the state of the file (with the right line for readline()
current_line += 1

# the next time that readline() is called, the state of the current line is
# preserved from the previous function call.  In this function call, the 
# line is line 2
print_a_line(current_line, current_file)

current_line += 1

print_a_line(current_line, current_file)
