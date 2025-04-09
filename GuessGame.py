import random

randNum = random.randint(1, 9)

playerGuess = input("Guess the random numer: ")

if playerGuess < randNum:
    print("Too low! Try again: ")

if playerGuess > randNum:
    print("Too high! Try again: ")