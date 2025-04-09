import random

randNum = random.randint(1, 9)

guesses = 0

playerGuess = input("Guess the random number: ")

while playerGuess != randNum:

    if playerGuess.lower() == "exit":
        exit()

    if int(playerGuess) < randNum:
        guesses += 1
        playerGuess = input("Too low! Try again or type 'exit' to quit: ")

    if int(playerGuess) > randNum:
        guesses += 1
        playerGuess = input("Too high! Try again or type 'exit' to quit: ")

    if int(playerGuess) == randNum:
        guesses += 1
        print(f"You guessed the correct number in {guesses} guesses!")

        randNum = random.randint(1, 9)
        playerGuess = input("Guess the random number or type 'exit' to quit: ")
