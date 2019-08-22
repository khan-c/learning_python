import os
from time import sleep

game = [["", "", "",],
        ["", "", "",],
        ["", "", "",],]
players = "O", "X"
current_player = "O"


def display_game_board():
    os.system('clear')
    print("   0   1   2")
    for count, row in enumerate(game):
        print(count, end="  ")
        for count, val in enumerate(row):
            if val == "" and count > 1:
                print()
            elif val == "":
                print(" ", end=" | ")
            elif count < 2:
                print(val, end=" | ")
            else:
                print(val)

def make_move(current_player):
    row, col = prompt_move()
    try:
        game[int(row)][int(col)] = current_player
    except ValueError:
        print("That input was not valid. Try again.")
        make_move(current_player)
    except IndexError:
        print("Needs to be a valid row/col!")
        make_move(current_player)

def prompt_move():
    global current_player
    print(current_player + ", make your move!")
    row = input("Row: ")
    col = input("Col: ")
    return row, col

def change_current_player():
    # how do you deal with scope in python?
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def check_win():
    return check_horizontal(game) or check_vertical(game) or check_diagonal(game)

def check_equality(arr):
    return all(arr) and arr.count(arr[0]) == len(arr)

def check_horizontal(game_board):
    for row in game_board:
        if all(row):
            if check_equality(row):
                return True
            else:
                continue
    return False

def check_vertical(game_board):
    t_game = zip(*game_board)
    return check_horizontal(t_game)

def check_diagonal(game_board):
    ltr = []
    rtl = []
    for x in range(len(game_board)):
        ltr.append(game_board[x][x])
        rtl.append(game_board[x][len(game_board) - x - 1])

    return check_equality(ltr) or check_equality(rtl)

def run_game():
    game_won = False
    while not game_won:
        change_current_player()
        display_game_board()
        make_move(current_player)
        game_won = check_win()

    display_game_board()
    print(current_player + " wins!")

run_game()