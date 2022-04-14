"""
This is the working file containing all the example and code challenges
presented during today's session.
"""

import os


def blind_auction():
	print("Welcome to the secret auction program.\n")
	bids = {}
	more_bidders = True
	while more_bidders:
		name = input("What is your name? ")
		amount = int(input("What is your bid? "))
		bids[name] = amount
		
		another_bidder = input("\nAre there any other bidders (y/n)? ")
		if another_bidder == 'n':
			more_bidders = False
		else:
			os.system('clear')

	max_bid = {
		'name': '',
		'amount': 0,
	}
	for bidder in bids:
		if bids[bidder] > max_bid['amount']:
			max_bid['name'] = bidder
			max_bid['amount'] = bids[bidder]

	os.system('clear')
	print(f"The winner is {max_bid['name']} with a bid of ${max_bid['amount']}")


def grading_program():
	student_scores = {
		'Harry': 81,
		'Ron': 78,
		'Hermione': 99,
		'Draco': 74,
		'Neville': 62,
	}
	
	student_grades = {}
	
	for student in student_scores:
		if student_scores[student] >= 91:
			student_grades[student] = 'Outstanding'
		elif student_scores[student] >= 81:
			student_grades[student] = 'Exceeds Expectations'
		elif student_scores[student] >=71:
			student_grades[student] = 'Acceptable'
		else:
			student_grades[student] = 'Fail'
	
	print(student_grades)


def nesting():
	travel_log = {
		'France': {
			'cities_visitied': ['Paris', 'Lille', 'Dijon'],
			'total_visits': 12
		},
	}

	print(travel_log)
	print(travel_log['France'])
	print(travel_log['France']['cities_visitied'])


def nesting_exercise():
	travel_log = [
		{
			'country': 'France',
			'visits': 12,
			'cities': ['Paris', 'Lille', 'Dijon']
		},
		{
			'country': 'Germay',
			'visits': 5,
			'cities': ['Berlin', 'Hamburg', 'Stuttgart']
		},
	]

	def add_new_country(country, visits, cities):
		new_country = {
			'country': country,
			'visits': visits,
			'cities': cities,
		}
		travel_log.append(new_country)

	
	add_new_country('Russia', 2, ['Moscow', 'Saint Petersburg'])

	for entry in travel_log:
		print(entry)


def run():
	print("Day 9 Exercises\n")
	blind_auction()
	# grading_program()
	# nesting()
	# nesting_exercise()