from random import randint
start_board = [
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [-1,0,-1,0,-1,0,-1,0],
    [0,-1,0,-1,0,-1,0,-1],
    [-1,0,-1,0,-1,0,-1,0]
]

remaining = [12,12]
                
def find_moves(board,team):
    reg_moves = []
    take_moves = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == team:
                for k in [-1,1]:
                    if i+team in range(8) and j+k in range(8):
                        if board[i+team][j+k] == 0:
                            reg_moves.append([[i,j],[i+team,j+k]])
                        elif board[i+team][j+k] == -1*team:
                            if i+2*team in range(8) and j+2*k in range(8):
                                if board[i+2*team][j+2*k] == 0:
                                    take_moves.append([[i,j],[i+2*team,j+2*k]])
            if board[i][j] == 2*team:
                for k in [-1,1]:
                    for l in [-1,1]:
                        if i+l in range(8) and j+k in range(8):
                            if board[i+l][j+k] == 0:
                                reg_moves.append([[i,j],[i+l,j+k]])
                            elif board[i+l][j+k] == -1*team:
                                if i+2*team in range(8) and j+2*k in range(8):
                                    if board[i+2*l][j+2*k] == 0:
                                        take_moves.append([[i,j],[i+2*l,j+2*k]])
    if len(take_moves) > 0:
        return ["take",take_moves]
    else:
        return ["reg",reg_moves]

def make_move(moves,board,team):
    if len(moves[1]) > 0:
        move_index = randint(0,len(moves[1])-1)
        my_move = moves[1][move_index]
        board[my_move[0][0]][my_move[0][1]] = 0
        board[my_move[1][0]][my_move[1][1]] = team
        if moves[0] == "take":
            enemy_x = (my_move[1][0] - my_move[0][0])/2 + my_move[0][0]
            enemy_y = (my_move[1][1] - my_move[0][1])/2 + my_move[0][1]
            board[enemy_x][enemy_y] = 0
        if team == -1 and my_move[1][0] == 0:
            board[my_move[1][0]][my_move[1][1]] = -2
        elif team == 1 and my_move[1][0] == 7:
            board[my_move[1][0]][my_move[1][1]] = 2
        return[board,my_move]
    else:
        return "loss"
    
def play_game():
    con = True
    team = -1
    board = start_board
    while con:
        moves = find_moves(board,team)
        made_move = make_move(moves,start_board,team)
        if made_move == "loss":
            print("loss by team "+str(team))
            con = False
        else:
            board = made_move[0]
            print board
            team = team * -1
    
play_game()