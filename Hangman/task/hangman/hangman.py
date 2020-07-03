# Write your code here
import random

word = ['python', 'java', 'kotlin', 'javascript']
game_word = random.choice(word)
num_hyphens = len(game_word) - 3
print("H A N G M A N")
guess = input(f"Guess the word {game_word[:3] + '-' * num_hyphens}: ")
print("You survived!") if guess == game_word else print("You are hanged!")