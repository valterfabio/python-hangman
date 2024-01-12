import random

def print_solution(solution):
    print(" ".join(solution))

word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)

solution = ["_" for _ in chosen_word]
print_solution(solution)

guess = input("Guess a letter: ").lower()
print([guess==letter for letter in chosen_word])

for i, letter in enumerate(chosen_word):
    if letter != "_" and letter == guess:
        solution[i] = letter

print_solution(solution)
