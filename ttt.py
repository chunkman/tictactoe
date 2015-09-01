#This is the worst code I've ever written

board = [['7','|','8','|','9'],['4','|','5','|','6'],['1','|','2','|','3']]
game_board_div = "----------"

def printgameboard():

    rowcount = 0
    print '\n'
    for row in board:
        for each in row:
            print each,
        rowcount += 1
        if rowcount <= 2:
            print '\n' + game_board_div
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

#def check_square(square):
#
#    return square.isdigit()

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

printgameboard()
letter = raw_input("Do you want to be X or O? ")
letter = letter.upper()
while (not (letter == 'X' or letter =='O')):
    letter = raw_input("Please enter an X or an O. ")
    letter = letter.upper()

board_total = 9

while (win_cond() == False):

    print "It is %s's turn." % letter
    keypad_num = int(raw_input("Enter the number of the square you want. "))
    while (keypad_num < 1 or keypad_num > 9):
        keypad_num = int(raw_input("Please enter a number between 1 and 9. "))
    valid_play = play_square(keypad_num, letter)
    while (valid_play == False):
        keypad_num = int(raw_input("That square is already taken. Choose another. "))
        valid_play = play_square(keypad_num, letter)
    printgameboard()
    board_total -= 1
    if board_total == 0:
        print "It is a tie!"
        break

    if letter == 'X':
        letter = 'O'
    elif letter == 'O':
        letter = 'X'

if win_cond():
    print "%s has won!" % win_cond()
