"""
This is the working file containing all the example and code challenges
presented during today's session.
"""
import random
import os

def play_hangman():
	list_of_words = ['barbeque', 'corvette', 'spaghetti', 'miscellanous']
	selected_word = random.choice(list_of_words)
	word_display = []
	for char in selected_word:
		word_display.append('_')

	bad_guesses = []
	remaining_guesses = 6
	while remaining_guesses > 0 and '_' in word_display:
		print(' '.join(word_display))
		print()
		print(f"Guesses remaining: {remaining_guesses}")
		if bad_guesses:
			print(f"Misses: {' '.join(bad_guesses)}")
		print()
		guess = input("Guess a letter: ").lower()
		os.system('clear')
		if guess in selected_word:
			if guess in word_display:
				print(f"You already guessed {guess}")
			else:
				for n in range(len(selected_word)):
					if selected_word[n] == guess:
						word_display[n] = selected_word[n]
				print(f"{guess} is in the word")
		else:
			print(f"{guess} is not in the word")
			bad_guesses.append(guess)
			remaining_guesses -= 1
		print()
		
	if not '_' in word_display:
		os.system('clear')
		print(f"The word is {selected_word}")
		print("You win!")
	elif remaining_guesses == 0:
	 	print("You lose")
	else:
		print("This is a bug!")


def run():
	print("Day 7 Exercises\n")
	play_hangman()
