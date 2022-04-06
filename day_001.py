"""
This is the working file containing all the example and code challenges
presented during today's session.
"""

def band_name_generator():
	# This is the Day 1 activity
	print("Welcome to the Band Name Generator.")
	city_name = input("What's the name of city you grew up in?\n")
	pet_name = input("What's your pet's name?\n")
	# return "Your band name could be " + city_name + " " + pet_name
	# It seems that using an f-string is pretty nice and makes the code more readable 
	return f"Your band name could be {city_name} {pet_name}"


def print_test():
	# You can print a " inside other "" using an escape "\" before the ".
	print("print(\"what to print\")")


def debugging_practice():
	print("Day 1 - String Manipulation")
	print("String Concatenation is done with the \"+\" sign.")
	print("e.g. print(\"Hello \" + \"world\")")
	print("New lines can be created with a backslash and n.")


def nested_input():
	# You can next an input statement inside a print statement
	print("Hello " + input("What is your name? ") + ". It's nice to meet you.")


def input_string_length():
	input_string = input("Enter a string: ")
	print(f"The string \"{input_string}\" is {len(input_string)} characters long.")


def variable_exercise():
	a = input("a: ")
	b = input("b: ")

	c = a
	a = b
	b = c

	print(f"a: {a}")
	print(f"b: {b}")


def run():
	print("Day 1 Exercises\n")
	print(band_name_generator())
	# print_test()
	# debugging_practice()
	# nested_input()
	# input_string_length()
	# variable_exercise()