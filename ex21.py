def add(a, b):
	print "Adding %d + %d" %(a, b)
	return a + b

def subtract(a, b):
	print "Subtracting %d - %d" %(a, b)
	return a - b

def multiply(a, b):
	print "Multiplying %d * %d" %(a, b)
	return a * b

def divide(a, b):
	print "Dividing %d / %d" %(a, b)
	return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)

print ("here is a puzzle.")

# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# yes I can
# print "That becomes: ", what, "Can you do it by hand?"

# normal formula

new_iq = divide(iq, 2)
new_weight = multiply(weight, new_iq)
new_height = subtract(height, new_weight)
what = add(age, new_height)

print what