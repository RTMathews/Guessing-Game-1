import random

randNum = random.randint(1, 9)

guesses = 0

playerGuess = int(input("Guess the random number: "))

while playerGuess != randNum:

    if playerGuess < randNum:
        guesses + 1
        playerGuess = int(input("Too low! Try again or type 'exit' to quit: "))

    elif playerGuess > randNum:
        guesses + 1
        playerGuess = int(input("Too high! Try again or type 'exit' to quit: "))

    elif playerGuess == randNum:
        guesses + 1
        print(f"You guessed the correct number in {guesses} guesses!")

        randNum = random.randint(1, 9)
        playerGuess = int(input("Guess the random number or 'exit' to quit: "))

    elif playerGuess == "exit":
        exit

    