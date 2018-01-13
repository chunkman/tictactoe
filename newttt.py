class Piece(object):
    def __init__(self,letter,space):
        
        self.letter = letter
        self.space = space - 1
        
        if letter == 'X':
            self.value = 1
        else:
            self.value = 4
        
player1_piece = Piece('X',5)
player2_piece = Piece('O',3)
game_board = ['1','2','3','4','5','6','7','8','9']
score_board = [0,0,0,0,0,0,0,0]
value_board = [0,0,0,0,0,0,0,0,0]

game_board[player1_piece.space] = player1_piece.letter
value_board[player1_piece.space] = player1_piece.value
game_board[player2_piece.space] = player2_piece.letter
value_board[player2_piece.space] = player2_piece.value

score_board[0] = value_board[0] + value_board[4] + value_board[8]
score_board[1] = value_board[0] + value_board[3] + value_board[6]
score_board[2] = value_board[1] + value_board[4] + value_board[7]
score_board[3] = value_board[2] + value_board[5] + value_board[8]
score_board[4] = value_board[2] + value_board[4] + value_board[6]
score_board[5] = value_board[0] + value_board[1] + value_board[2]
score_board[6] = value_board[3] + value_board[4] + value_board[5]
score_board[7] = value_board[6] + value_board[7] + value_board[8]


print game_board[0] + '|' + game_board[1] + '|' + game_board[2] + '\n'
print '-----------------------' + '\n'
print game_board[3] + '|' + game_board[4] + '|' + game_board[5] + '\n'
print '-----------------------' + '\n'
print game_board[6] + '|' + game_board[7] + '|' + game_board[8] + '\n'

print "score_board = ", score_board
print "value_board = ", value_board
