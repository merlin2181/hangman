# Write your code here
import random
import string


def check_input(text, listofguess):
    if len(text) < 1 or len(text) > 1:
        print("You should input a single letter")
        return 1
    if text not in string.ascii_lowercase:
        print("It is not an ASCII lowercase letter")
        return 1
    if text in listofguess:
        print("You already typed this letter")
        return 1
    return 0


word = ['python', 'java', 'kotlin', 'javascript']
game_word = random.choice(word)
set_word = set(game_word)
output = list('-' * len(game_word))
lives = 8
guesses = []
print("H A N G M A N")
while lives > 0:
    print("""
{}""".format(''.join(output)))
    guess = input("Input a letter: ")
    check = check_input(guess, guesses)
    guesses.append(guess)
    if check == 1:
        continue
    if guess in set_word:
        for i in range(len(game_word)):
            if game_word[i] == guess:
                output[i] = guess
    else:
        print("No such letter in the word")
        lives -= 1
    name = ("".join(output))
    if name == game_word:
        print("""You guessed the word {}!
You survived!""".format(game_word))
        break
    if lives == 0:
        print("You are hanged!")
