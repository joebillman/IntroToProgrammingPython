import os
import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

gameIsFinished = False
lives = len(stages) - 1

chosenWord = random.choice(word_list)
wordLength = len(chosenWord)

display = []

for char in range(0, wordLength):
    display += "_"

def clearScreen():
    os.system("cls")

while not gameIsFinished:
    guess = input("Guess a letter: ").lower()

    clearScreen()

    gameIsFinished = True
