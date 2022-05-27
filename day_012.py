"""
This is the working file containing all the example and code challenges
presented during today's session.
"""

import os
import random


EASY_GUESSES = 10
HARD_GUESSES = 5


def set_difficulty():	
	response = int(input("Type 1 for easy and 2 for hard: "))
	return EASY_GUESSES if response == 1 else HARD_GUESSES
	

def game_loop():
	number_to_guess = random.randint(1,100)
	guesses = set_difficulty()
	guesses_made = 0
	guesses_remaining = guesses
	guessed_correctly = False
	print(f"\nYou have {guesses} guesses")
	print(f"The number to guess is {number_to_guess}")

	while not guessed_correctly:
		if guesses_remaining == 0:
			print("\nToo many guesses. You lose.")
			break
		else:
			guess = int(input("\nMake a guess: "))
			guesses_made += 1
			guesses_remaining = guesses - guesses_made

		if guess == number_to_guess:
			guess_tense = 'guesses' if guesses_made > 1 else 'guess'
			print(f"\nYou got it in {guesses_made} {guess_tense}!")
			guessed_correctly = True
		elif guess > number_to_guess:
			print(f"\nToo high. You have {guesses_remaining} guesses remaining")
		elif guess < number_to_guess:
			print(f"\nToo low. You have {guesses_remaining} guesses remaining")
		else:
			print("\nWhat is going on here?")
			guessed_correctly = True
			

def number_guessing_game():
	print("\nNumber Guessing Game")
	print("\nGuess a number from 1 to 100")
	keep_playing = True
	
	while keep_playing:
		game_loop()
		play_again = input("\nPlay again? 'y' or 'n' ")
		if play_again == 'n':
			keep_playing = False
		os.system('clear')


def run():
	print("Exercises for Day 12")
	number_guessing_game()
	