®import random

#: Lastenheft:


#: Logik definieren, was schlägt was
#: Spieler gibt ein Input ein Wert ein ( r, p, s) - Input Check
#: CPU wählt random aus Schere, Stein, Papier - Anschließend Auswertung wer gewonnen hat
#: Best of 3 gewinnt - Siege aufzeichnen
#: Neues Spiel anfangen?

print("""
RULES - Best of 3
↳ If you win 2 time you win.

Put in one of the following options when it's your turn:

s - ✂️
r - 🧱
p - 📃
""")

def new_game():
    while True:
        answer = input("Do you want to start a new game? (y/n) ").lower()
        if answer == "y":
            game_init()
        elif answer == "n":
            print("All right, see you next time!")
            break
        else:
            print("You have to type 'y' or 'n' to continue.")

def who_wins(user_input, cpu_input): #: return win or draw
    if user_input == cpu_input:
        return "draw"
    elif user_input == "s" and cpu_input == "r" or user_input == "r" and cpu_input == "p" or user_input == "p" and cpu_input == "s":
        return  "cpu"
    else:
        return "user"

def game_init():
    player_score = 0
    cpu_score = 0
    options = {"r": "🧱", "s": "✂️", "p": "📃"}
    input_options = [x for x in options]
    round_counter = 0
    while True:
        round_counter += 1
        print("Round No.", round_counter)
        cpu_input = random.choice(input_options)
        while True:
            user_input = input("What's your move?: ").lower()
            if user_input in input_options:
                break
            else:
                print("Oops. Wrong input... Try 's', 'r' or 'p'.")
        print(f"User: {options.get(user_input)} vs. {options.get(cpu_input)} :CPU")
        result = who_wins(user_input, cpu_input)
        if result == "cpu":
            cpu_score += 1
            print("CPU wins.")
            if cpu_score >= 2:
                print("Score:", player_score, cpu_score)
                break
        elif result == "user":
            player_score += 1
            print("Player wins.")
            if player_score >= 2:
                print("Score:", player_score, cpu_score)
                break
        else:
            print("No winner.")


    new_game()


game_init()



