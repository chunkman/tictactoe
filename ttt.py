# TODO Add docstrings
# TODO Add difficulty select
# TODO Split functions to seperate file?

import string
import os
import random

game_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
available_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
score_board = [0, 0, 0, 0, 0, 0, 0, 0]
value_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

player1_letter = 'X'
player2_letter = 'O'
player1_value = 1
player2_value = 4


def human_play(letter, value):

    space = raw_input("%s: Enter space number: " % letter)

    space = check_number(space)

    while space not in available_squares:

        print "That square is already taken. Please choose another."
        space = raw_input("%s: Enter space number: " % letter)
        space = check_number(space)

    game_board[space - 1] = letter

    value_board[space - 1] = value

    available_squares.remove(space)

    set_score_board()


def computer_play(letter, value):

    if value is 1:

        enemy_value = 4
    else:

        enemy_value = 1

    space = hard_mode(value, enemy_value)

    game_board[space - 1] = letter

    value_board[space - 1] = value

    available_squares.remove(space)

    set_score_board()


def check_number(space):

    while space[0] not in string.digits:

        print "Please enter a number between 1 and 9"
        space = raw_input("Enter space number: ")

    return int(space[0])


def set_score_board():

    score_board[0] = value_board[0] + \
        value_board[4] + value_board[8]  # Left Diagonal
    score_board[1] = value_board[0] + \
        value_board[3] + value_board[6]  # Left Column
    score_board[2] = value_board[1] + \
        value_board[4] + value_board[7]  # Center Column
    score_board[3] = value_board[2] + \
        value_board[5] + value_board[8]  # Right Column
    score_board[4] = value_board[2] + value_board[4] + \
        value_board[6]  # Right Diagonal
    score_board[5] = value_board[0] + \
        value_board[1] + value_board[2]  # Top Row
    score_board[6] = value_board[3] + \
        value_board[4] + value_board[5]  # Middle Row
    score_board[7] = value_board[6] + \
        value_board[7] + value_board[8]  # Bottom Row


def print_game_board():

    if win_condition() == False:

        os.system('cls' if os.name == 'nt' else 'clear')

    print '\n'
    print "     " + game_board[0] + '|' + game_board[1] + '|' + game_board[2]
    print '    --------'
    print "     " + game_board[3] + '|' + game_board[4] + '|' + game_board[5]
    print '    --------'
    print "     " + game_board[6] + '|' + game_board[7] + '|' + game_board[8]
    print '\n'


def win_condition():

    if 3 in score_board:

        print "X Wins!\n"
        return True

    elif 12 in score_board:

        print "O Wins\n"
        return True

    elif 0 not in value_board:

        print "It's a Tie!"
        return True

    else:

        return False


def hard_mode(my_value, enemy_value):

    if 5 in available_squares:
        return 5
    elif 2 * enemy_value in score_board:
        return two_row(enemy_value)
    elif 2 * my_value in score_board:
        return two_row(my_value)
    elif compare_lists([1, 3, 7, 9], available_squares):
        return compare_lists([1, 3, 7, 9], available_squares)
    else:
        return random.choice(available_squares)


def compare_lists(list1, list2):

    matches = []

    for i in list1:
        if i in list2:
            matches.append(i)

    if matches == []:
        return False
    else:
        return random.choice(matches)


def two_row(value):

    value *= 2

    if score_board.index(value) is 0:
        return compare_lists([1, 5, 9], available_squares)
    elif score_board.index(value) is 1:
        return compare_lists([1, 4, 7], available_squares)
    elif score_board.index(value) is 2:
        return compare_lists([2, 5, 8], available_squares)
    elif score_board.index(value) is 3:
        return compare_lists([3, 6, 9], available_squares)
    elif score_board.index(value) is 4:
        return compare_lists([3, 5, 7], available_squares)
    elif score_board.index(value) is 5:
        return compare_lists([1, 2, 3], available_squares)
    elif score_board.index(value) is 6:
        return compare_lists([4, 5, 6], available_squares)
    elif score_board.index(value) is 7:
        return compare_lists([7, 8, 9], available_squares)


num_of_players = raw_input("Enter the number of players: 1 or 2.")

if num_of_players == '1':

    while True:

        print_game_board()
        human_play(player1_letter, player1_value)
        if win_condition():
            break

        print_game_board()
        computer_play(player2_letter, player2_value)
        if win_condition():
            break

elif num_of_players == '2':

    while True:

        print_game_board()
        human_play(player1_letter, player1_value)
        if win_condition():
            break

        print_game_board()
        human_play(player2_letter, player2_value)
        if win_condition():
            break

elif num_of_players == '0':

    while True:

        print_game_board()
        computer_play(player1_letter, player1_value)
        if win_condition():
            break

        print_game_board()
        computer_play(player2_letter, player2_value)
        if win_condition():
            break

print_game_board()
