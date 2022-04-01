def treasure_island():
	print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
	print("Welcome to Treasure Island.")
	print("Your mission is to find the treasure.")

	choice1 = input("You\'re at a cross road. Where do you want to go? Type \"left\" or \"right\" \n").lower()
	if choice1 == 'left':
	  choice2 = input("You\'ve come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n").lower()
	  if choice2 == 'wait':
	    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? \n").lower()
	    if choice3 == 'red':
	      print("It's a room full of fire. Game Over.")
	    elif choice3 == 'yellow':
	      print("You found the treasure! You Win!")
	    elif choice3 == 'blue':
	      print("You enter a room of beasts. Game Over.")
	    else:
	      print("You chose a door that doesn't exist. Game Over.")
	  else:
	    print("You get attacked by an angry trout. Game Over.")
	else:
	  print("You fell into a hole. Game Over.")


def even_or_odd():
	test_number = int(input("Enter a whole number: "))
	if test_number % 2 == 0:
		print("This is an even number")
	else:
		print("This is an odd number")


def check_is_leap_year():
	test_year = int(input("Enter a year: "))
	is_leap_year = False
	
	if test_year % 4 == 0: #is a leap year
		if test_year % 100 == 0: # is not a leap year
			if test_year % 400 == 0: # is a leap year
				is_leap_year = True
			else:
				is_leap_year = False
		else:
			is_leap_year = True
	else:
		is_leap_year = False

	if is_leap_year:
		print(f"{test_year} is a leap year")
	else:
		print(f"{test_year} is not a leap year")	


def love_calculator():
	your_name = input("Enter your name: ")
	their_name = input("Enter their name: ")
	combined_name = your_name + their_name

	love_score = 0
	
	for char in 'true':
		love_score += combined_name.lower().count(char)
	love_score *= 10

	for char in 'love':
		love_score += combined_name.lower().count(char)
	
	if love_score < 10 or love_score > 90:
		print(f"Your score is {love_score}, you go together like coke and mentos")
	elif love_score >= 40 and love_score <= 50:
		print(f"Your score is {love_score}, you are alright together.")
	else:
		print(f"Your score is {love_score}.")
	

def run():
	print("Day 3 Exercises")
	print()
	treasure_island()
	# even_or_odd()
	# check_is_leap_year()
	# love_calculator()