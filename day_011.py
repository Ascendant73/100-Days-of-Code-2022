"""
This is the day 11 capstone project.
Blackjack
"""

import os
import random


def draw_a_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(cards)


def calculate_hand_total(hand):
	hand_total = sum(hand)
	# enumerate() allows me to get the index and the value at the same time without needing to loop one and manually track the other.
	# https://realpython.com/python-enumerate/
	for index, card in enumerate(hand):
		if hand_total > 21 and card == 11:
			hand[index] = 1
			hand_total = sum(hand)
	return hand_total


def play_blackjack():
	players_hand = []
	computers_hand = []

	# The '_' in this context is a convention to signify that the index is not important.
	# It's just needed to do the loop x times. Could be any other variable name.
	for _ in range(2): 
		players_hand.append(draw_a_card())
		computers_hand.append(draw_a_card())

	print(f"\nYour cards: {players_hand}")
	print(f"Comupter's first card: [{computers_hand[0]}]\n")
	
	another_card = True
	while another_card:
		hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
		if hit_me == 'y':
			players_hand.append(draw_a_card())
			print(f"\nYour cards: {players_hand}")
		else:
			another_card = False
	
	players_total = calculate_hand_total(players_hand)
	computers_total = calculate_hand_total(computers_hand)
	while computers_total < 17:
		computers_hand.append(draw_a_card())
		computers_total = calculate_hand_total(computers_hand)

	print(f"\nYour final hand: {players_hand}")
	print(f"Computer's final hand: {computers_hand}\n")

	if players_total > 21:
		print("Bust! You lose!\n")
	elif computers_total > 21:
		print("The Computer busted! You win!\n")
	elif players_total > computers_total:
		print("You win!\n")
	elif players_total == computers_total:
		print("Tie\n")
	else:
		print("You lose!\n")


def blackjack_intro():
	play_again = True
	while play_again:
		play_yn = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
		os.system('clear')
		if play_yn == 'y':
			play_blackjack()
		else:
			print("Thank's for playing! Goodbye")
			play_again = False


def run():
	print("Day 11 Capstone\n")
	blackjack_intro()
