#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

# Function to initialize a new deck
def initialize_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Function to calculate the total value of a hand
def calculate_total(hand):
    total = 0
    num_aces = 0

    for card in hand:
        if card['rank'] in ['J', 'Q', 'K']:
            total += 10
        elif card['rank'] == 'A':
            total += 11
            num_aces += 1
        else:
            total += int(card['rank'])

    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1

    return total

# Function to simulate a round of Blackjack
def play_round():
    deck = initialize_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    while True:
        print(f"Player's hand: {player_hand} (Total: {calculate_total(player_hand)})")
        action = input("Do you want to hit or stay? ").lower()

        if action == 'hit':
            player_hand.append(deck.pop())
            if calculate_total(player_hand) > 21:
                print("Bust! You lose.")
                return 'dealer'
        elif action == 'stay':
            break

    while calculate_total(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    print(f"\nPlayer's hand: {player_hand} (Total: {calculate_total(player_hand)})")
    print(f"Dealer's hand: {dealer_hand} (Total: {calculate_total(dealer_hand)})")

    if calculate_total(dealer_hand) > 21 or calculate_total(player_hand) > calculate_total(dealer_hand):
        print("Congratulations! You win!")
        return 'player'
    else:
        print("Dealer wins. Better luck next time.")
        return 'dealer'

# Function to run multiple rounds and compare results
def run_simulations(num_simulations):
    player_wins = 0
    dealer_wins = 0

    for _ in range(num_simulations):
        result = play_round()
        if result == 'player':
            player_wins += 1
        elif result == 'dealer':
            dealer_wins += 1

    print(f"\nResults after {num_simulations} simulations:")
    print(f"Player wins: {player_wins}")
    print(f"Dealer wins: {dealer_wins}")

# Example: Run 100 simulations
run_simulations(100)


# In[ ]:
