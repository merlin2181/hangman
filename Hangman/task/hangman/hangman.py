# Write your code here
import random
import string


def check_input(text, listofguess):
    if len(text) != 1:
        print("You should input a single letter")
        return True
    if text not in string.ascii_lowercase:
        print("It is not an ASCII lowercase letter")
        return True
    if text in listofguess:
        print("You already typed this letter")
        return True
    return False


word = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
while True:
    game_word = random.choice(word)
    set_word = set(game_word)
    output = list('-' * len(game_word))
    lives = 8
    guesses = set()
    while True:
        keep_going = input('Type "play" to play the game, "exit" to quit: ')
        if keep_going != "play" and keep_going != "exit":
            continue
        else:
            break
    if keep_going == "play":
        while lives > 0:
            print("""
{}""".format(''.join(output)))
            guess = input("Input a letter: ")
            if check_input(guess, guesses):
                continue
            if guess in set_word:
                for i in range(len(game_word)):
                    if game_word[i] == guess:
                        output[i] = guess
                        guesses.add(guess)
            else:
                print("No such letter in the word")
                guesses.add(guess)
                lives -= 1
            name = ("".join(output))
            if name == game_word:
                print("""You guessed the word {}!
You survived!
""".format(game_word))
                break
            if lives == 0:
                print("""You are hanged!
""")
    else:
        break
