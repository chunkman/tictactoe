#This is the worst code I've ever written
#Note for future me: try using a dict to hold the values of the board.
import random


board = [
            ['7','|','8','|','9'],
            ['4','|','5','|','6'],
            ['1','|','2','|','3']
        ]

def printgameboard():

    rowcount = 0
    print '\n'
    for row in board:
        for each in row:
            print each,
        rowcount += 1
        if rowcount <= 2:
            print '\n' + '----------'
    print '\n'

def win_cond():

    if board[0][0] == board[0][2] == board[0][4]:
        return board[0][0]
    elif board[1][0] == board[1][2] == board[1][4]: 
        return board[1][0]
    elif board[2][0] == board[2][2] == board[2][4]:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    elif board[0][4] == board[1][4] == board[2][4]:
        return board[0][4]
    elif board[0][0] == board[1][2] == board[2][4]:
        return board[0][0]
    elif board[0][4] == board[1][2] == board[2][0]:
        return board[0][4]
    else:
        return False


def play_square(number, letter):

    if number == 1 and board[2][0].isdigit():
        board[2][0] = letter
        return True
    elif number == 2 and board[2][2].isdigit():
        board[2][2] = letter
        return True
    elif number == 3 and board[2][4].isdigit():
        board[2][4] = letter
        return True
    elif number == 4 and board[1][0].isdigit():
        board[1][0] = letter
        return True
    elif number == 5 and board[1][2].isdigit():
        board[1][2] = letter
        return True
    elif number == 6 and board[1][4].isdigit():
        board[1][4] = letter
        return True
    elif number == 7 and board[0][0].isdigit():
        board[0][0] = letter
        return True
    elif number == 8 and board[0][2].isdigit():
        board[0][2] = letter
        return True
    elif number == 9 and board[0][4].isdigit():
        board[0][4] = letter
        return True
    else:
        return False

def player_turn(letter):

    keypad_num = raw_input("Enter the number of the square you want: ")
    while keypad_num not in '123456789':
        keypad_num = raw_input("Please enter a number between 1 and 9: ")
    keypad_num = int(keypad_num)
    valid_play = play_square(keypad_num, letter)
    while valid_play == False:
        while keypad_num not in '123456789':
            keypad_num = raw_input("Please enter a number between 1 and 9: ")
        keypad_num = int(keypad_num)
        valid_play = play_square(keypad_num, letter)

def cpu_turn(letter):

    keypad_num = random.randint(1, 10)
    valid_play = play_square(keypad_num, letter)
    while valid_play == False:
        keypad_num = random.randint(1, 10)
        valid_play = play_square(keypad_num, letter)


printgameboard()
num_players = int(raw_input("How many players? 1 or 2."))
if num_players == 1:

    while True:

        print "X's Turn"
        player_turn('X')
        printgameboard()
        if win_cond():
            print 'X wins'
            break
        print "O's Turn"
        cpu_turn('O')
        printgameboard()
        if win_cond():
            print 'O wins'
            break
else:
    while True:

        print "X's Turn"
        player_turn('X')
        printgameboard()
        if win_cond():
            print 'X wins'
            break
        print "O's Turn"
        player_turn('O')
        printgameboard()
        if win_cond():
            print 'O Wins'
            break


