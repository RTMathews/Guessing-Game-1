import random

randNum = random.randint(1, 9)

guesses = 0

playerGuess = input("Guess the random numer: ")

if playerGuess < randNum:
    guesses + 1
    print("Too low! Try again: ")

if playerGuess > randNum:
    guesses + 1
    print("Too high! Try again: ")

if playerGuess == randNum:
    guesses + 1
    print("You guess the correct number!")