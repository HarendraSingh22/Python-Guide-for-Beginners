# guess my number game : computer generates a random number between 0 and 100, player has to guess the right number
# muemmelmoehre, 10/2017

import random

print('Welcome to the game "Guess my number"!')
numberToGuess = random.randint(0,100)

print("PC chose a number between 0 and 100.")
counter = 0
guessIsCorrect = False

while(guessIsCorrect != True):
    guessPlayer = int(input("Please enter your guess : "))
    if (guessPlayer == numberToGuess):
        counter += 1
        guessIsCorrect = True
        print("Congratulations! It took you only", counter, "guesses to get the right number.")
    elif (guessPlayer < numberToGuess):
        counter += 1
        print("Your number is too small. Please try again.")
    elif (guessPlayer > numberToGuess):
        counter += 1
        print("Your number is too big. Please try again.")

