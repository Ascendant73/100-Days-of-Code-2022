def tip_calculator():
	print("Welcome to the time calculator.\n")
	total_bill = float(input("What was the total bill? "))
	tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15? ")) / 100
	split_count = int(input("How many people to split the bill? "))
	each_pay_amount = "${:,.2f}".format(total_bill * (1.0 + tip_percentage) / split_count)
	print(f"Each person sohuld pay: {each_pay_amount}")


def print_test():
	# Python will ignore the _ in large integers. This is just to make it easier to read for people
	print("{:,}".format(123_456_789))
	print(7//3) # // is the integer divsion operator
	print()
	
	# string_var = 'Hello Tutorialspoint'
	# print("\"%s\"" % string_var )
	# print("\\%s\\" % string_var )
	# print('"%s"' % string_var )
	# print('"{}"'.format(string_var))
	# print("\"{}\"".format(string_var))

	print(8/3)
	print(8//3)
	print(round(8/3))
	print(round(8/3, 2))
	

def add_two_digits():
	two_digit_number = input("Type a two digit number: ")
	print(int(two_digit_number[0]) + int(two_digit_number[1]))


def bmi_calculator():
	# My weight = 83.914 & my height = 1.778m 
	height = float(input("Enter your height in meters: "))
	weight = float(input("Enter your weight in kilograms: "))
	bmi = int(weight / height ** 2)
	print(f"Your BMI is {bmi}")


def life_in_weeks():
	current_age = input("What is your current age: ")
	years_till_90 = 90 - int(current_age)
	months_till_90 = years_till_90 * 12
	weeks_till_90 = years_till_90 * 52
	days_till_90 = years_till_90 * 365
	message = f"You have {days_till_90} days, {weeks_till_90} weeks, and {months_till_90} months left"
	print(message)


def run():
	print("Day 2 Exercises")
	print()
	tip_calculator()
	# print_test()
	# add_two_digits()
	# bmi_calculator()
	# life_in_weeks()