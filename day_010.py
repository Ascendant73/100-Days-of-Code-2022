"""
This is the working file containing all the example and code challenges
presented during today's session.
"""


def my_calculator():
	"""This is a docstring test"""
	
	def do_calculation(number_1, operand, number_2):
		if operand == '+':
			return number_1 + number_2
		elif operand == '-':
			return number_1 - number_2
		elif operand == '*':
			return number_1 * number_2
		elif operand == '/':
			return number_1 / number_2

	keep_repeating = True
	have_result = False
	result = None

	while keep_repeating:
		if have_result:
			print(f"\nThe first number is {result}")
			first_number = result
		else:
			first_number = float(input("\nWhat is the first number? "))
		operation = input("Pick an opertation (+ - * /) ")
		second_number = float(input("What is the second number? "))

		result = do_calculation(first_number, operation, second_number)
		
		if result:
			print(f"\n{first_number} {operation} {second_number} = {result}\n")
			
		answer = input(f"Type 'y' to continue calculating with {result}\nType 'n' to start a new calcuation\nType 'q' to quit: ")
		
		if answer == 'y':
			have_result = True
		elif answer == 'n':
			have_result = False
			result == None
		else:
			print("\nGoodbye!")
			break

def her_calculator():
	def add(n1, n2):
		return n1 + n2

	def subtract(n1, n2):
		return n1 - n2

	def multiply(n1, n2):
		return n1 * n2

	def divide(n1, n2):
		return n1 / n2

	operations = {
		'+': add,
		'-': subtract,
		'*': multiply,
		'/': divide,
	}

	def do_calculation():
	
	  num1 = float(input("What's the first number?: "))
	  for symbol in operations:
	    print(symbol)
	  should_continue = True
	 
	  while should_continue:
	    operation_symbol = input("Pick an operation: ")
	    num2 = float(input("What's the next number?: "))
	    calculation_function = operations[operation_symbol]
	    answer = calculation_function(num1, num2)
	    print(f"{num1} {operation_symbol} {num2} = {answer}")
	
	    if input(f"Type 'y' to continue calculating with {answer},\nor type 'n' to start a new calculation: ") == 'y':
	      num1 = answer
	    else:
	      should_continue = False
	      do_calculation()

	do_calculation()
		

def run():
	print("Day 10 Exercises\n")
	# my_calculator()
	her_calculator()