import random

randNum = random.randint(1, 9)

guesses = 0

playerGuess = int(input("Guess the random numer: "))

while playerGuess != randNum:

    if playerGuess < randNum:
        guesses + 1
        playerGuess = int(input("Too low! Try again: "))

    if playerGuess > randNum:
        guesses + 1
        print("Too high! Try again: ")

    if playerGuess == randNum:
        guesses + 1
        print(f"You guessed the correct number in {guesses} guesses!")