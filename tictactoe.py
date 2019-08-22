import os
from time import sleep
import itertools

game_size = 3
game = []
player = itertools.cycle(["X", "O"])
current_player = player

def initialize_game():
    global game_size
    global game

    print("Welcome to Tic Tac Toe!")
    try:
        game_size = int(input("What game board size would you like? (ie. 3x3, 4x4)"))
    except ValueError:
        print("Invalid input. Try again.")
        initialize_game()

    # is this the python way? make things one-line? kind of like ruby?
    game = [["" for i in range(game_size)] for i in range(game_size)]
    # for _ in range(game_size):
    #     row = []
    #     for _ in range(game_size):
    #         row.append("")
    #     game.append(row)
    # print(game)

def display_game_board():
    os.system('clear')
    column_header = "   " + "   ".join([str(i) for i in range(game_size)])
    # for i in range(game_size):
    #     column_header += str(i) + "   "
    print(column_header)
    for count, row in enumerate(game):
        print(count, end="  ")
        for count, val in enumerate(row):
            if val == "" and count == game_size - 1:
                print()
            elif val == "":
                print(" ", end=" | ")
            elif count != game_size - 1:
                print(val, end=" | ")
            else:
                print(val)

def make_move(current_player):
    raw_row, raw_col = prompt_move()
    try:
        row = int(raw_row)
        col = int(raw_col)
        if not spot_taken(row, col):
            game[row][col] = current_player
        else:
            print("That spot is taken. Try again.")
            make_move(current_player)
    except ValueError:
        print("That input was not valid. Try again.")
        make_move(current_player)
    except IndexError:
        print("Needs to be a valid row/col!")
        make_move(current_player)

def spot_taken(row, col):
    return game[row][col] is not ""

def prompt_move():
    print(current_player + ", make your move!")
    row = input("Row: ")
    col = input("Col: ")
    return row, col

def change_current_player():
    # confused a bit about this global thing... maybe too used to javascript variable declarations
    global current_player
    current_player = next(player)

'''
design decision would be if in a game of greater than size 3
would we want it to be a full row/column/diag in order to win,
or just 3 in a row anywhere?
'''
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
    initialize_game()
    game_won = False
    while not game_won:
        change_current_player()
        display_game_board()
        make_move(current_player)
        game_won = check_win()

    display_game_board()
    print(current_player + " wins!")

run_game()