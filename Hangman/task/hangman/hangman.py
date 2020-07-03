# Write your code here
import random

word = ['python', 'java', 'kotlin', 'javascript']
game_word = random.choice(word)
set_word = set(game_word)
output = list('-' * len(game_word))
attempts = 8
print("H A N G M A N")
while attempts > 0:
    print("""
{}""".format(''.join(output)))
    guess = input("Input a letter: ")
    if guess in set_word:
        for i in range(len(game_word)):
            if game_word[i] == guess:
                output[i] = guess
        attempts -= 1
    else:
        print("No such letter in the word")
        attempts -= 1
print("""
Thanks for playing!
We'll see how well you did in the next stage""")