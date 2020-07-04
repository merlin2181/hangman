# Write your code here
import random

word = ['python', 'java', 'kotlin', 'javascript']
game_word = random.choice(word)
set_word = set(game_word)
output = list('-' * len(game_word))
lives = 8
print("H A N G M A N")
while lives > 0:
    print("""
{}""".format(''.join(output)))
    guess = input("Input a letter: ")
    if guess in set_word:
        if guess in output:
            print("No improvements")
            lives -= 1
        else:
            for i in range(len(game_word)):
                if game_word[i] == guess:
                    output[i] = guess
    else:
        print("No such letter in the word")
        lives -= 1
    if output == game_word:
        print("""You guessed the word!
You survived!""")
        break
    if lives == 0:
        print("You are hanged!")