# -*- coding: utf-8 -*-
import random


def display_board(board):
    for i in range(0, 7, 3):
        print(' ' + board[i] + ' | ' + board[i+1] + ' | ' + board[i+2])
        if i != 6:
            print('-----------')


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ->').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or  # across the top
            (board[3] == mark and board[4] == mark and board[5] == mark) or  # across the middle
            (board[6] == mark and board[7] == mark and board[8] == mark) or  # across the bottom
            (board[0] == mark and board[3] == mark and board[6] == mark) or  # down the left side
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # down the middle
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # down the right side
            (board[0] == mark and board[4] == mark and board[8] == mark) or  # diagonal
            (board[2] == mark and board[4] == mark and board[6] == mark))  # diagonal


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(9):
        if space_check(board, i):
            return False
    return True


def player_choice(board, turn):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)-1):
        position = input(turn + ' choose your next position: (1-9) ')
    return int(position)-1


def replay():
    return input('Do you want to play again? Enter Yes or No ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    the_board = [' '] * 9
    player1_marker, player2_marker = player_input()
    print('Player 1 marker - > ' + player1_marker + '\n' + 'Player 2 marker - > ' + player2_marker)
    turn = choose_first()
    print(turn + ' will go first')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board, turn)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Congratulation! Player 1 have won the game')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board, turn)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Congratulation! Player 2 have won the game')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
