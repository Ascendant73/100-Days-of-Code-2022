"""
Day 13 is focused on debugging

Step 1: Describe the problem
Step 2: Reproduce the error

Nothing new here. All these examples were pretty obvious.
"""

import os


def debug_odd_even():
	number = int(input("Which number do you want to check? "))

	if number % 2 == 0:
	  print("This is an even number.")
	else:
	  print("This is an odd number.")


def debug_leap_year():
	year = int(input("Which year do you want to check? "))

	if year % 4 == 0:
	  if year % 100 == 0:
	    if year % 400 == 0:
	      print("Leap year.")
	    else:
	      print("Not leap year.")
	  else:
	    print("Leap year.")
	else:
	  print("Not leap year.")


def debug_fizzbuzz():
	for number in range(1, 101):
		if number % 3 == 0 and number % 5 == 0:
			print("FizzBuzz")
		elif number % 3 == 0:
			print("Fizz")
		elif number % 5 == 0:
			print("Buzz")
		else:
			print(number)


def run():
	os.system('clear')
	print("Day 13 Debugging Exercises")
	# debug_odd_even()
	# debug_leap_year()
	debug_fizzbuzz()