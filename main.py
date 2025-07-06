import random
"""
Advanced Dice Rolling Game

This script implements a dice rolling game where the user can play multiple rounds.
In each round, the user rolls two dice and scores points based on the sum of the dice.
If the user rolls doubles (both dice show the same number), they receive a bonus of 5 points.
The total score is displayed at the end of the game.

Features:
- User selects the number of rounds to play.
- Each round, the user rolls two dice.
- Points are awarded equal to the sum of the dice.
- Rolling doubles awards an additional 5 bonus points.
- Final score is displayed after all rounds.

Usage:
Run the script and follow the prompts to play the game.
"""

# Advanced Dice Rolling Game - A game where the user can roll two dice multiple times and score points based on the rolls.
# The user can choose how many rounds to play, and they earn points based on the total of the dice rolled.
print("Welcome to the Advanced Dice Rolling Game!")

rounds = int(input("How many rounds would you like to play? "))
score = 0

for i in range(1, rounds + 1):
    input(f"\nRound {i}: Press Enter to roll the dice...")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print(f"You rolled: ({dice1}, {dice2}) - Total: {total}")

    if dice1 == dice2:
        print("Doubles! Bonus 5 points!")
        score += 5
    score += total

print(f"\nThanks for playing! Your final score is: {score}")
