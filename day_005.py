"""
This is the working file containing all the example and code challenges
presented during today's session.
"""

import random

def password_generator():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	print("Welcome to the PyPassword Generator!\n")
	pw_letters = int(input(f"How many letters would you like in your password? ")) 
	pw_symbols = int(input(f"How many symbols would you like? "))
	pw_numbers = int(input(f"How many numbers would you like? "))
	pw_length = pw_letters + pw_numbers + pw_symbols
	print()
	
	password = ''
	for char in range(pw_length):
		next_char = random.randint(1,3)
		if next_char == 2 and pw_numbers > 0:
			password += random.choice(numbers)
			pw_numbers -= 1
		elif next_char == 3 and pw_symbols > 0:
			password += random.choice(symbols)
			pw_symbols -= 1
		else:
			password += random.choice(letters)
		
	print(f"Your password is {password}")

	# Anohter approach
	#	Get all the letters, numbers, and symbols into a list
	#	Use random.shuffle(list) to suffle the elements
	#	Convert the list into a string with the ''.join(list) or a for loop
	# pw_list = []
	# for char in password:
	# 	pw_list.append(char)
	# print(pw_list)
	# random.shuffle(pw_list)
	# pw_str = ''.join(pw_list)
	# print(pw_str)
	

def find_average_height():
	int_list = [1, 2, 3, 4, 5]
	print(int_list)
	print(sum(int_list))

	# sum() does not work on strigs. It is intended to work on numbers only!
	# str_list = ['a', 'b', 'c', 'd', 'e']
	# print(str_list)
	# print(sum(str_list))
	
	# the .split() with no arguments will split the string on any whitespace
	student_heights = input("Enter the list of student heights, separated by a space ' ': \n").split()

	# There is a differnce between looping through the indices of a list and the values of a list
	# This is looking through the indices
	for n in range(len(student_heights)):
		student_heights[n] = int(student_heights[n])
	
	all_student_heights = 0
	student_count = 0

	# There is a differnce between looping through the indices of a list and the values of a list
	# This is looping through the values
	for student_height in student_heights:
		all_student_heights += student_height
		student_count += 1

	print()
	print(f"There are {len(student_heights)} students")
	print(f"The total height for all students is {sum(student_heights)}")
	print()
	print(f"There are {student_count} students")
	print(f"The average student height is {all_student_heights // student_count}")


def find_highest_score():
	scores = input("Enter the list of scores: ").split()

	# Unlike sum(), the min() and max() work with strings as well as numbers
	print(f"The min(scores) = {min(scores)}")
	print(f"The max(scores) = {max(scores)}")

	for n in range(len(scores)):
		scores[n] = int(scores[n])

	highest_score = 0
	for score in scores:
		if score > highest_score:
			highest_score = score

	print(f"The highest score is {highest_score}")


def adding_even_numbers():
	sum_of_even = 0
	for n in range(2, 100+1, 2):
		# print(f"The current number is {n}")
		sum_of_even += n

	print(sum_of_even)


def fizzbuzz():
	for n in range(1, 100+1):
		if n % 3 == 0 and n % 5 == 0:
			print("FizzBuzz")
		elif n % 3 == 0:
			print("Fizz")
		elif n % 5 == 0:
			print("Buzz")
		else:
			print(n)

	# Here are a couple of other examples of how to accomplish this task 
	# https://towardsdatascience.com/4-easy-ways-to-beat-fizz-buzz-in-python-cfa2dcb9b813


def run():
	print("Day 5 Exercises\n")
	password_generator()
	# find_average_height()
	# find_highest_score()
	# adding_even_numbers()
	# fizzbuzz()