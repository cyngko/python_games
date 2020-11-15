#: Hangman Game
import random
from projects import words_csv

word_pool = words_csv.import_words()


def new_game():
    while True:
        answer = input("Do you want to start a new game? (y/n) ").lower()
        if answer == "y":
            return game_init()
        elif answer == "n":
            return print("All right, see you next time!")
        else:
            print("You have to type 'y' or 'n' to continue.")


def game_init():
    magic_word = random.choice(word_pool).lower()
    placeholder = []
    for i in magic_word:
        if i == "-":
            placeholder.append(i)
        else:
            placeholder.append("_")
    lives = 9
    round_num = 1
    used_letters = []
    while lives > 0:
        print(f"Round {round_num}")
        round_num += 1
        print(f"Lives left: {lives}")
        display_magic_word = "".join(placeholder).capitalize()
        print(display_magic_word)
        if display_magic_word.lower() == magic_word:
            print('Congrats! You won.')
            break

        allowed_input = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                         "t", "u", "v", "x", "y", "z", "ä", "ö", "ü", "ß"]
        while True:
            guess = input("Gib einen Buchstaben ein: ").lower()
            if guess in allowed_input:
                break
            else:
                print("Input is not allowed. Try again.")
        used_letters.append(guess)
        print("Letters used so far:", used_letters)
        if guess in magic_word:
            print("Correct! Keep going.")
            letter_pos = [x for x, y in enumerate(magic_word) if y == guess]
            for pos in letter_pos:
                placeholder[pos] = guess
        else:
            lives -= 1
            print("Not this one! Try again.")


    if lives <= 0:
        print(f"Sorry you lost the game. The magic word was: {magic_word}")
    new_game()


game_init()

