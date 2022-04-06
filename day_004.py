"""
This is the working file containing all the example and code challenges
presented during today's session.
"""

import random


def rock_paper_scissors():
	player_choice = int(input("Choose 0 for rock, 1 for paper, or 2 for scissors: "))
	computer_choice = random.randint(0,2)

	if player_choice < 0 or player_choice >3:
		print("You type an invalid character. You lose!")
		return
		
	choices = ['rock', 'paper', 'scissors']
	print(f"You choose {choices[player_choice]}")
	print(f"The computer choose {choices[computer_choice]}")

	if player_choice == 0 and computer_choice == 2:
		print("You win!")
	elif computer_choice == 0 and player_choice == 2:
		print("You lose!")
	elif computer_choice > player_choice:
		print("You lose!")
	elif player_choice > computer_choice:
		print("You win!")
	elif player_choice == computer_choice:
		print("It's a draw.")

	
def learn_random():
	random_int = random.randint(1, 10)
	print(random_int)
	random_float = random.random()
	print(random_float)


def heads_tails():
	random_int = random.randint(0,1)
	if random_int == 1:
		print("Heads")
	else:
		print("Tails")


def learn_lists():
	us_states = ['Deleware', 'Pennsylvania', 'New Jersey']
	print(us_states)
	print(us_states[0])
	print(us_states[-1])
	print()
	us_states.append('New York')
	print(us_states)
	print(us_states[0])
	print(us_states[-1])


def banker_roulette():
	input_string = input("Enter a list of names, separated by a comma and space (, ):\n")
	bankers_names = input_string.split(', ')
	random_choice = random.randint(0, len(bankers_names) - 1)
	print(f"{bankers_names[random_choice]} has to pay for lunch!")
	# random.choice()
	# https://docs.python.org/3.8/library/random.html?highlight=choice#random.choice
	print(f"{random.choice(bankers_names)} has to pay for lunch!")


def nested_lists():
	inner_list_1 = ['a', 'b']
	inner_list_2 = [1, 2]
	outer_list = [inner_list_1, inner_list_2]
	print(outer_list)
	print(outer_list[0][1])


def treasure_map():
	row1 = [' ', ' ', ' ']
	row2 = [' ', ' ', ' ']
	row3 = [' ', ' ', ' ']
	map = [row1, row2, row3]
	print(f"{row1}\n{row2}\n{row3}")
	print()
	position = input("Where do you want to put the treasure? ")
	print()
	column = int(position[0]) - 1
	row = int(position[1]) - 1
	map[row][column] = 'X'
	print(f"{row1}\n{row2}\n{row3}")
	

def run():
	print("Day 4 Exercises\n")
	rock_paper_scissors()
	# learn_random()
	# heads_tails()
	# learn_lists()
	# banker_roulette()
	# nested_lists()
	# treasure_map()