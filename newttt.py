#TODO: Add Hard difficulty level.

import string
import os
import random

game_board = ['1','2','3','4','5','6','7','8','9']
score_board = [0,0,0,0,0,0,0,0]
value_board = [0,0,0,0,0,0,0,0,0]

player1_letter = 'X'
player2_letter = 'O'
player1_value = 1
player2_value = 4

def human_play(letter,value):

    space = raw_input("%s: Enter space number: " % letter)
    
    space = check_number(space)
    
    while check_play(space) == False:

        print "That square is already taken. Please choose another."
        space = raw_input("%s: Enter space number: " % letter)
        space = check_number(space)

    game_board[space - 1] = letter

    value_board[space - 1] = value
    
    set_score_board()

def computer_play(letter,value):

    space = random.randint(1, 9)

    while check_play(space) == False:

        space = random.randint(0, 9)

    game_board[space - 1] = letter

    value_board[space - 1] = value

    set_score_board()

def check_number(space):

    while(space not in string.digits):

        print "Please enter a number between 1 and 9"
        space = raw_input("Enter space number: ")

    return int(space)

def check_play(space):

    if value_board[space - 1] == 0:

        return True

    else:

        return False

def set_score_board():

    score_board[0] = value_board[0] + value_board[4] + value_board[8]
    score_board[1] = value_board[0] + value_board[3] + value_board[6]
    score_board[2] = value_board[1] + value_board[4] + value_board[7]
    score_board[3] = value_board[2] + value_board[5] + value_board[8]
    score_board[4] = value_board[2] + value_board[4] + value_board[6]
    score_board[5] = value_board[0] + value_board[1] + value_board[2]
    score_board[6] = value_board[3] + value_board[4] + value_board[5]
    score_board[7] = value_board[6] + value_board[7] + value_board[8]

def print_game_board():

    if(win_condition() == False):

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

num_of_players = raw_input("Enter the number of players: 1 or 2.")

if num_of_players == '1':

    while True:

        print_game_board()
        human_play(player1_letter, player1_value)
        if win_condition() == True:
            break

        print_game_board()
        computer_play(player2_letter, player2_value)
        if win_condition() == True:
            break

elif num_of_players == '2':

    while True:

        print_game_board()
        human_play(player1_letter, player1_value)
        if win_condition() == True:
            break

        print_game_board()
        human_play(player2_letter, player2_value)
        if win_condition() == True:
            break

elif num_of_players == '0':

    while True:

        print_game_board()
        computer_play(player1_letter,player1_value)
        if win_condition() == True:
            break

        print_game_board()
        computer_play(player2_letter,player2_value)
        if win_condition() == True:
            break
else:

    print "You are an idiot."

print_game_board()    
