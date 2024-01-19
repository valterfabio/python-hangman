import os
import random
from printables import logo, stages
from string import ascii_uppercase
from words import word_list

def clean_console():
    return os.system('cls')

def print_solution(solution):
    print(" ".join(solution), end="\n\n")

allowed_letters = set(ascii_uppercase)
guessed_letters = set()

chosen_word = random.choice(word_list).upper()
solution = ["_" for _ in chosen_word]
mistakes = 0
has_won = False

clean_console()
print(logo)

while (mistakes < 6) and (has_won is False):

    print(stages[mistakes])
    print_solution(solution)
    guess = input("Guess a letter: ").upper()
    clean_console()

    if guess not in allowed_letters:
        print(f"Please, choose only letters! The character '{guess}' is not allowed!")

    elif guess in guessed_letters:
        print(f"You have already chosen the letter '{guess}'. Chose another one!")

    else:
        guessed_letters.add(guess)
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                solution[i] = letter

        if "_" not in solution:
            has_won = True

        if guess not in chosen_word:
            print(f"\nThe letter {guess} is not in the word! You lost a life! \U0001F615")
            mistakes += 1

if has_won:
    print(f"YOU WON! \U0000270C \nThe word was {chosen_word}! \U0001F600\n")
else:
    print(stages[mistakes])
    print(f"YOU LOST! \U0001F616 \nThe word was {chosen_word}!\n")
