#game_board_top = [' ','|',' ','|',' ']
#game_board_mid = [' ','|',' ','|',' ']
#game_board_bot = [' ','|',' ','|',' ']
#game_board_div = "---------"

game_board = [[' ','|',' ','|',' '],[' ','|',' ','|',' '],[' ','|',' ','|',' ']]
game_board_div = "----------"

def printgameboard(board):

    for row in board:
        for each in row:
            print each,
        print '\n' + game_board_div
    print '\n'

def win_cond(board):

    if board[0][0] == board[0][2] == board[0][4]:
        print "Row 1 win"
    elif board[1][0] == board[1][2] == board[1][4]:
        print "Row 2 win"
    elif board[2][0] == board[2][2] == board[2][4]:
        print "Row 3 win"
    elif board[0][0] == board[1][0] == board[2][0]:
        print "Column 1 win"
    elif board[0][2] == board[1][2] == board[2][2]:
        print "Column 2 win"
    elif board[0][4] == board[1][4] == board[2][4]:
        print "Column 3 win"
    elif board[0][0] == board[1][2] == board[2][4]:
        print "Diagonal 1 win"
    elif board[0][4] == board[1][2] == board[2][0]:
        print "Diagonal 2 win"

