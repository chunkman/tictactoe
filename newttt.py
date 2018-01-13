import string

game_board = ['1','2','3','4','5','6','7','8','9']
score_board = [0,0,0,0,0,0,0,0]
value_board = [0,0,0,0,0,0,0,0,0]

player1_letter = 'X'
player2_letter = 'O'
player1_value = 1
player2_value = 4

def player1_play():

    player1_space = raw_input("X: Enter space number: ")

    while(player1_space not in string.digits):
            print "Please enter a number between 1 and 9"
            player1_space = raw_input("X: Enter space number: ")

    player1_space = int(player1_space)

    game_board[player1_space-1] = player1_letter
    value_board[player1_space-1] = player1_value
    
    set_score_board()

def player2_play():

    player2_space = raw_input("O: Enter space number: ")
    
    while(player2_space not in string.digits):
        print "Please enter a number between 1 and 9"
        player2_space = raw_input("O: Enter space number: ")

    player2_space = int(player2_space)

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
    if 3 in score_board:
        print "X Wins!\n"
        return True
    elif 12 in score_board:
        print "O Wins\n"
        return True

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
