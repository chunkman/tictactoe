        
game_board = ['1','2','3','4','5','6','7','8','9']
score_board = [0,0,0,0,0,0,0,0]
value_board = [0,0,0,0,0,0,0,0,0]

player1_letter = 'X'
player2_letter = 'O'
player1_value = 1
player2_value = 4

def player1_play():

    player1_space = int(raw_input("Player One: Enter space number: "))
    
    game_board[player1_space-1] = player1_letter
    value_board[player1_space-1] = player1_value
    
    set_score_board()

def player2_play():

    player2_space = int(raw_input("Player Two: Enter space number: "))

    game_board[player2_space-1] = player2_letter
    value_board[player2_space-1] = player2_value
    
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

    if 0 not in value_board:
        print "It's a Tie!"
        return True
    for each in score_board:
        if each == 3:
            print "X Wins!"
            return True
        elif each == 12:
            print "O Wins!"
            return True
        else:
            return False

while(True):

    print_game_board()
    player1_play()
    if win_condition():
        break
    print_game_board()
    player2_play()
    if win_condition():
        break
    
print_game_board()

   # print "score_board = ", score_board
   # print "value_board = ", value_board
