import random

board = ["⬜️", "⬜️", "⬜️",
         "⬜️", "⬜️", "⬜️",
         "⬜️", "⬜️", "⬜️"]

board_example = [str(x) for x in range(1, 10)]

name_player1 = input("Player 1: Wie heißt du?: ")
name_player2 = input("Player 2: Wie heißt du?: ")

symbol_player1 = input(f"{name_player1}: Such dir dein Symbol aus: ")
symbol_player2 = input(f"{name_player2}: Such dir dein Symbol aus: ")

player = [name_player1, name_player2]

def display_board(display):
    print("")
    print("|" + display[0] + "|" + display[1] + "|" + display[2] + "|")
    print("|" + display[3] + "|" + display[4] + "|" + display[5] + "|")
    print("|" + display[6] + "|" + display[7] + "|" + display[8] + "|")
    print("")



print(f"""
{name_player1}: {symbol_player1}
{name_player2}: {symbol_player2}

Gib eine Zahl zwischen 1 - 9 an. 
""")
print("Board:")
display_board(board_example)


def new_game_init():
    while True:
        answer = input("Neues Spiel beginnen? (j/n) ").lower()
        if answer == "j":
            return game_init()
        elif answer == "n":
            return print("Alles klar, bis zum nächsten Mal!")
        else:
            print("Du musst 'j' oder 'n' eingeben um fortzufahren.")


def game_init():
    board = ["⬜️", "⬜️", "⬜️",
             "⬜️", "⬜️", "⬜️",
             "⬜️", "⬜️", "⬜️"]
    current_player = random.choice(player)
    winner = None
    display_board(board)
    while winner is None:
        while True:
            try:
                player_input = input(f"{current_player}: ")
                if int(player_input) not in range(1, 10):
                    print("Dieses Feld existiert nicht. Versuch es nochmal.")
                    continue
                if board[int(player_input) - 1] == "⬜️":
                    if current_player == name_player1:
                        board[int(player_input) - 1] = symbol_player1
                        pass
                    else:
                        board[int(player_input) - 1] = symbol_player2
                        pass
                else:
                    print("Da kannst du nicht hin. Probiere es nochmal...")
                    continue
                display_board(board)

                player1_wins = [symbol_player1, symbol_player1, symbol_player1]
                player2_wins = [symbol_player2, symbol_player2, symbol_player2]
                winning_condition = [[board[0], board[1], board[2]],
                                     [board[3], board[4], board[5]],
                                     [board[6], board[7], board[8]],
                                     [board[0], board[3], board[6]],
                                     [board[1], board[4], board[7]],
                                     [board[2], board[5], board[8]],
                                     [board[0], board[4], board[8]],
                                     [board[2], board[4], board[6]],
                                     ]
                if player1_wins in winning_condition:
                    print(f"GAME OVER. {current_player} hat gewonnen!")
                    return new_game_init()
                elif player2_wins in winning_condition:
                    print(f"GAME OVER. {current_player} hat gewonnen!")
                    return new_game_init()
                if "⬜️" not in board:
                    return print("GAME OVER. Das Spiel endet unentschieden.")
                if current_player == name_player1:
                    current_player = name_player2
                else:
                    current_player = name_player1

            except ValueError:
                 print("Das geht leider nicht. Versuche es nochmal ...")


game_init()