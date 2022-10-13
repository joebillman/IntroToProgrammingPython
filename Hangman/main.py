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
lettersGuessed = []

for char in range(0, wordLength):
    display += "_"

def clearScreen():
    os.system("cls")

while not gameIsFinished:
    alreadyGuessed = False
    guess = input("Guess a letter: ").lower()

    clearScreen()

    if guess in lettersGuessed:
        print(f"You've already guessed {guess}")
        alreadyGuessed = True

    if guess not in lettersGuessed:
        lettersGuessed.append(guess)
        
    print(f"Letters guessed: {lettersGuessed}")
    
    for position in range(0, wordLength):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = guess
    print(f"{' '.join(display)}")

    if alreadyGuessed == False:
        if guess not in chosenWord:
            print(f"You guessed {guess}, that's not in the word.")
            lives -= 1
            if lives == 0:
                gameIsFinished = True
                print(f"Game Over. You lost. The word was: {chosenWord}")
        if not "_" in display:
            gameIsFinished = True
            print("Game Over YOU WON!")
    print(stages[lives])
        