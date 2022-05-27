"""
This is the working file containing all the example and code challenges
presented during today's session.
"""

import math


def caesar_cipher():
	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	symbols = [' ', '.', ',', '?', '!', ':', ';' ]
	base_chars = uppercase + lowercase + numbers + symbols

	def create_offset(starting_chars, offset):
		offset %= len(starting_chars)
		if offset != 0:
			start_of_list = starting_chars[:-offset or None]
			end_of_list = starting_chars[-offset or None:]
			new_chars = end_of_list + start_of_list
		else:
			new_chars = starting_chars
		return new_chars	

	def encode_or_decode(operation, base_chars):
		message = input(f"\nWhat is the message to {operation}?\n")
		offset = int(input("\nWhat is the offset?\n"))
		
		if operation == 'decode':
			starting_chars = create_offset(base_chars, offset)
			offset *= -1
		else:
			starting_chars = base_chars
			
		offset_chars = create_offset(starting_chars, offset)
		
		message_output = ""
		for char in message:
			char_index = starting_chars.index(char)
			message_output += offset_chars[char_index]

		print(f"\nThe original message is {message}")
		print(f"The {operation}d message is {message_output}")

	go_again = True
	while go_again:
		operation = input("Type 'encode' to encrypt, type 'decode' to decrypt, or type 'quit' to quit:\n").lower()
		# if operation == 'encode' or operation == 'decode':
		if operation in {'encode', 'decode'}:
			encode_or_decode(operation, base_chars)
		elif operation == 'quit':
			go_again = False
		else:
			print("Invalid Command")
			go_again = False
		print()
	
	
def paint_area_calc():
	def cans_of_paint(height, width, coverage=5):
		return math.ceil((height * width) / coverage)
		
	height = int(input("What is wall height? "))
	width = int(input("What is wall width? "))
	print(f"You will need {cans_of_paint(height, width)} cans of paint.")


def prime_number_checker():
	def prime_checker(check_number):
		zero_count = 0
		for n in range(1, check_number + 1):
			# print(f"{check_number} % {n} = {check_number % n}")
			if check_number % n == 0:
				zero_count += 1
				
		if zero_count == 2:
			print(f"{check_number} is a prime number.")
		else:
			print(f"{check_number} is not a prime number.")
			
	prime_checker(int(input("Number to check: ")))


def run():
	print("Day 8 Exercises\n")
	caesar_cipher()
	# paint_area_calc()
	# prime_number_checker()