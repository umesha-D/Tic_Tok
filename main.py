

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

game_still_going = True
winner = None
current_Player = "x"


def display_board():
    print(board[0] + "| " + board[1] + "|" + board[2])
    print(board[3] + "| " + board[4] + "|" + board[5])
    print(board[6] + "| " + board[7] + "|" + board[8])


def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_Player)

        check_if_game_over()

        flip_player()


    if winner == "x" or winner == "o":
        print(winner + " won")
    elif winner == None:
         print("Tie")


def handle_turn(player):


    print(player + "s turn.")
    position = input("choose a position from 1-9: ")

    valid = False
    while not valid:

     while position not in ["1", "2","3","4","5","6","7","8","9"]:
        position = input("invalid input choose a position from 1-9")

     position = int(position) - 1

     if board[position] == "_":
        valid = True
     else:
        print("You cant go there , go again")

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    global winner

    row_winner = check_rows()
    column_winner = check_coloums()
    diagonas_winner = check_diagonas()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonas_winner:
        winner = diagonas_winner
    else:
        winner = None

    return


def check_rows():
    global  game_still_going
    row_1 = board[0] == board[1] == board[2]!="_"
    row_2 = board[3] == board[4] == board[5]!="_"
    row_3 = board[6] == board[7] == board[8]!="_"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_coloums():
    global game_still_going
    coloums_1 = board[0] == board[3] == board[6] != "_"
    coloums_2 = board[1] == board[4] == board[7] != "_"
    coloums_3 = board[2] == board[5] == board[8] != "_"

    if coloums_1 or coloums_2 or coloums_3:
        game_still_going = False

    if coloums_1:
        return board[0]
    elif coloums_2:
        return board[1]
    elif coloums_3:
        return board[2]
    return


def check_diagonas():

    global game_still_going
    diagonas_1 = board[0] == board[4] == board[8] != "_"
    diagonas_2 = board[6] == board[4] == board[2] != "_"


    if diagonas_1 or diagonas_2 :
        game_still_going = False

    if diagonas_1:
        return board[0]
    elif diagonas_2:
        return board[6]

    return


def check_if_tie():

    global game_still_going
    if "_" not in board:
        game_still_going = False
    return


def flip_player():
    global  current_Player

    if current_Player == "x":
        current_Player ="o"
    elif current_Player == "o":
        current_Player = "x"
    return


play_game()
