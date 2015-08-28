
game_board = [[' ','|',' ','|',' '],[' ','|',' ','|',' '],[' ','|',' ','|',' ']]
game_board_div = "----------"

def printgameboard(board):

    print '\n'
    for row in board:
        for each in row:
            print each,
        print '\n' + game_board_div
    print '\n'

def win_cond(board):

    if board[0][0] == board[0][2] == board[0][4] != ' ':
        print "Row 1 win"
        return board[0][0]
    elif board[1][0] == board[1][2] == board[1][4] != ' ':
        print "Row 2 win"
        return board[1][0]
    elif board[2][0] == board[2][2] == board[2][4] != ' ':
        print "Row 3 win"
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0] != ' ':
        print "Column 1 win"
        return board[0][0]
    elif board[0][2] == board[1][2] == board[2][2] != ' ':
        print "Column 2 win"
        return board[0][2]
    elif board[0][4] == board[1][4] == board[2][4] != ' ':
        print "Column 3 win"
        return board[0][4]
    elif board[0][0] == board[1][2] == board[2][4] != ' ':
        print "Diagonal 1 win"
        return board[0][0]
    elif board[0][4] == board[1][2] == board[2][0] != ' ':
        print "Diagonal 2 win"
        return board[0][4]
    else:
        return False

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


while (win_cond(game_board) == False):

    x = int(raw_input("> "))
    letter = 'X'
    play_square(game_board,x,letter)
    win_cond(game_board)
    printgameboard(game_board)
