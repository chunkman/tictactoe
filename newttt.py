class Piece(object):
    def __init__(self,letter,space):
        
        self.letter = letter
        self.space = space - 1
        
        if letter == 'X':
            self.value = 1
        else:
            self.value = 4
        
game_board = ['1','2','3','4','5','6','7','8','9']
score_board = [0,0,0,0,0,0,0,0]
value_board = [0,0,0,0,0,0,0,0,0]

player1_letter = 'X'
player2_letter = 'O'

def player1_play():

    player1_space = int(raw_input("Enter space number: "))
    player1_piece = Piece(player1_letter,player1_space)
    
    game_board[player1_piece.space] = player1_piece.letter
    value_board[player1_piece.space] = player1_piece.value
    
    
    set_score_board()

def player2_play():

    player2_space = int(raw_input("Enter space number: "))
    player2_piece = Piece(player2_letter,player2_space)

    game_board[player2_piece.space] = player2_piece.letter
    value_board[player2_piece.space] = player2_piece.value
    
    
    set_score_board()

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
    print "-----------------------"
    print game_board[0] + '|' + game_board[1] + '|' + game_board[2]
    print '-----------------------' 
    print game_board[3] + '|' + game_board[4] + '|' + game_board[5] 
    print '-----------------------' 
    print game_board[6] + '|' + game_board[7] + '|' + game_board[8] 
    print '-----------------------' + '\n'

def win_condition():
    for each in score_board:
        if each == 3:
            print "X Wins!"
            return True
            break
        elif each == 12:
            print "O Wins!"
            return True
            break
while(True):

    print_game_board()
    player1_play()
    if win_condition() == True:
        break
    print_game_board()
    player2_play()
    if win_condition() == True:
        break

print_game_board()

   # print "score_board = ", score_board
   # print "value_board = ", value_board
