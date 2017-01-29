first_name = "Joseph"


def print_two(name, age):
	print("Your name is: %s" % name)
	print("Your age is: %d" % age)

def print_one(name):
	print("Your name is: %s" % name)

def print_none():
	print("I got nothin'")

#print_two("first_name, 27")
#print_one("Joseph")
#print_none()

def add(a, b):
	print("ADDING %d + %d" % (a, b))
	return a + b

def subtract(a, b):
	print("SUBTRACTING %d - %d" % (a, b))
	return a - b

def multiply(a, b):
	print("MULTIPLYING %d * %d" % (a, b))
	return a * b

def divide(a, b):
	print("DIVIDING %d / %d" % (a, b))
	return a / b

age = add(20,7)
weight = multiply(80,2)
height = subtract(76,6)
iq = divide(130,2)

print("Age: %d, Weight: %d, Height: %d, IQ: %d" % (age, weight, height, iq))