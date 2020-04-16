

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
                if i+team in range(8) and j+1 in range(8):
                    if board[i+team][j+1] == 0:
                        reg_moves.append([[i,j],[i+team,j+1]])
                    elif board[i+team][j+1] == -1*team:
                        if i+2*team in range(8) and j+2 in range(8):
                            if board[i+2*team][j+2] == 0:
                                take_moves.append([[i,j],[i+2*team,j+2]])
                if i+team in range(8) and j-1 in range(8):
                    if board[i+team][j-1] == 0:
                        reg_moves.append([[i,j],[i+team,j-1]])
                    elif board[i+team][j-1] == -1*team:
                        if i+2*team in range(8) and j-2 in range(8):
                            if board[i+2*team][j-2] == 0:
                                take_moves.append([[i,j],[i+2*team,j+2]])                    
	if len(take_moves) > 0:
        return take_moves
    else:
        return reg_moves
                
                
    
print(find_moves(start_board,1,2,1))