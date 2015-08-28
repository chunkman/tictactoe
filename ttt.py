#game_board_top = [' ','|',' ','|',' ']
#game_board_mid = [' ','|',' ','|',' ']
#game_board_bot = [' ','|',' ','|',' ']
#game_board_div = "---------"

game_board = [[' ','|',' ','|',' '],[' ','|',' ','|',' '],[' ','|',' ','|',' ']]
game_board_div = "--------"

def printgameboard(board):

    for row in board:
        for each in row:
            print each,
        print '\n' + game_board_div


printgameboard(game_board)
