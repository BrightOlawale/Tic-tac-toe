#!/usr/bin/python3


import random


def display_board(board):
    for row in range(3):
        print("+-------"*3, "+", sep="")
        print("|       "*4)
        for col in range(3):
            print(f"|   {str(board[row][col])}   ", end="")
        print("|")
        print("|       "*4)
    print("+-------"*3, "+", sep="")


def enter_move(board):
    try:
        move = int(input("Enter your move:\n"))
        if move < 1 or move > 9 or move == 5:
            raise ValueError
        for row in range(len(board)):
            for col in range(len(board[row])):
                if str(move) == board[row][col]:
                    board[row][col] = 'O'
                    return board
                continue
    except (TypeError, ValueError):
        print("Move must be a free integer(1-9)")
        return 0


def make_list_of_free_fields(board):
    move_options = []
    for row in range(len(board)):
        for space in range(len(board[row])):
            if str(board[row][space]) == 'O' or str(board[row][space]) == 'X':
                continue
            move_options.append(board[row][space])
    return(tuple(move_options))


def horizontal_check(board, sign):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == str(sign):
            return 1
    return 0


def vertical_check(board, sign):
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == str(sign):
            return 1
    return 0


def diagonal_check(board, sign):
    i = 0
    j = 0
    if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == str(sign):
        return 1
    elif board[i][j+2] == board[i+1][j+1] == board[j+2][i] == str(sign):
        return 1
    else:
        return 0


def victory_for(board, sign):
    result = horizontal_check(board, sign) or vertical_check(board, sign) or diagonal_check(board, sign)
    if result:
        return 1
    else:
        return 0


def draw_move(board):
    available = make_list_of_free_fields(board)
    move = random.choice(available)
    for row in range(len(board)):
        for col in range(len(board[row])):
            if str(move) == board[row][col]:
                board[row][col] = 'X'
                return board
            continue
