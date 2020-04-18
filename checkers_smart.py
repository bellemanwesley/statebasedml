from random import random
from random import randint
import copy
import json
import sys

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

def matrix_int(matrix,adder):
    result = ""
    for j in range(len(matrix)):
        for k in range(len(matrix[j])):
            result += str(adder+matrix[j][k])
    return result
                
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

def smart_move(dec_moves,moves):
    moves_dec = []
    for x in moves[1]:
        move_int = matrix_int(x,0)
        if move_int in dec_moves:
            move_hist = dec_moves[move_int]
            move_weight = float(move_hist[0])/(move_hist[0]+move_hist[1])
            else:
                move_weight = 0.5
            move_factor = move_weight * random()
            moves_dec.append(move_factor)
    move_index = moves_dec.index(max(moves_dec))
    return move_index
    
def make_move(moves,board,team,dec_dict):
    if len(moves[1]) > 0:
        board_int = matrix_int(board,2)
        if sys.argv[1] = "smart" and board_int in dec_dict:
            dec_moves = dec_dict[board_int]
            move_index = smart_move(dec_moves,moves[1])
        else:
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
    
def play_game(dec_dict):
    con = True
    team = -1
    board = copy.deepcopy(start_board)
    counter = 0
    boards_moves_plus = []
    boards_moves_minus = []    
    while con:
        counter += 1
        moves = find_moves(board,team)
        made_move = make_move(moves,board,team,dec_dict)
        if made_move == "loss":
            con = False
        elif counter>100:
            con = False
            return 200
        else:
            if team == 1:
                boards_moves_plus.append(copy.deepcopy([board,made_move[1]]))
            elif team == -1:
                boards_moves_minus.append(copy.deepcopy([board,made_move[1]]))
            board = made_move[0]
            team = team * -1
    for i in range(len(boards_moves_plus)):
        boards_moves_plus[i] = boards_moves_plus[i] + [team*-1]
    for i in range(len(boards_moves_minus)):
        boards_moves_minus[i] = boards_moves_minus[i] + [team]        
    return boards_moves_plus + boards_moves_minus

def dec_dict_update(boards_moves,dec_dict):
    for x in boards_moves:
        board_key = matrix_int(x[0],2)
        move_key = matrix_int(x[1],0)
        if board_key in dec_dict:
            if move_key in dec_dict[board_key]:
                print board_key
                print dec_dict[board_key]
                if x[2] == 1:
                    dec_dict[board_key][move_key][0] += 1
                elif x[2] == -1:
                    dec_dict[board_key][move_key][1] += 1
            else:
                if x[2] == 1:
                    dec_dict[board_key][move_key] = [2,1]
                elif x[2] == -1:
                    dec_dict[board_key][move_key] = [1,2]
        else:
            if x[2] == 1:
                dec_dict.update({board_key:{move_key:[2,1]}})
            elif x[2] == -1:
                dec_dict.update({board_key:{move_key:[1,2]}})
    return dec_dict
      
def check_command():
    fail_message = ''' 
    Fail message
    '''
    try:
        result = int(sys.argv[2])
        if sys.argv[1] not in ["smart","random"]:
            print fail_message
            exit(1)
        else:
            return result
    except:
        print fail_message
        exit(1)
    
def main():
    max_counter = check_command()
    dec_dict = {}
    over_counter = 0
    while over_counter < max_counter:
        game_results = play_game(dec_dict)
        if type(game_results) is not int:
            dec_dict = dec_dict_update(game_results,dec_dict)
        del game_results
        over_counter += 1
    with open('files/game_results.txt','w+') as f:
        json.dump(dec_dict,f)
                    
main()

                    