#!/usr/bin/python3


import brainbox


board = [['1', '2', '3'],
         ['4', 'X', '6'],
         ['7', '8', '9']]


choices = brainbox.make_list_of_free_fields(board)
while(len(choices)):
    brainbox.display_board(board)
    board = brainbox.enter_move(board)
    if board == 0:
        break
    status = brainbox.victory_for(board, 'O')
    if status == 1:
        brainbox.display_board(board)
        print("You won!\n")
        break
    else:
        brainbox.display_board(board)
    print("Computer's turn... press 1 to continue\n")
    entry = int(input("Enter: "))
    if entry == 1:
        board = brainbox.draw_move(board)
        # display_board(board)
        status = brainbox.victory_for(board, 'X')
        if status == 1:
            brainbox.display_board(board)
            print("Computer won!\n")
            break
    choices = brainbox.make_list_of_free_fields(board)
    if len(choices) == 0:
        brainbox.display_board(board)
        print("Draw!\n")
