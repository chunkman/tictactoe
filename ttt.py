
game_board = [['7','|','8','|','9'],['4','|','5','|','6'],['1','|','2','|','3']]
game_board_div = "----------"

def printgameboard(board):

    print '\n'
    for row in board:
        for each in row:
            print each,
        print '\n' + game_board_div
    print '\n'

def win_cond(board):

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

def check_square(square):
    if square != 'X' and square != 'O':
        return True

def play_square(board, number, letter):

    if number == 1:
        board[2][0] = letter
        return board
    elif number == 2:
        board[2][2] = letter
        return board
    elif number == 3:
        board[2][4] = letter
        return board
    elif number == 4:
        board[1][0] = letter
        return board
    elif number == 5:
        board[1][2] = letter
        return board
    elif number == 6:
        board[1][4] = letter
        return board
    elif number == 7:
        board[0][0] = letter
        return board
    elif number == 8:
        board[0][2] = letter
        return board
    elif number == 9:
        board[0][4] = letter
        return board

printgameboard(game_board)
letter = raw_input("Do you want to be X or O? ")
letter = letter.upper()

while (win_cond(game_board) == False):

    keypad_num = int(raw_input("Enter the number of the square you want."))
    game_board = play_square(game_board,keypad_num,letter)
    winning_letter = win_cond(game_board)
    printgameboard(game_board)
    if winning_letter:
        print "The letter %s wins!" % winning_letter
        break
    elif letter == 'X':
        letter = 'O'
    else:
        letter = 'X'
    print "It's %s's turn. " % letter
    
