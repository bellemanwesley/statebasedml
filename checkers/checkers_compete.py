from random import random
from random import randint
import copy
import json
import sys
import os
import time

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
    for x in moves:
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
    
def make_move(moves,board,team,dec_dict, state_transform):
    if len(moves[1]) > 0:
        board_int = state_getter(board, state_transform)
        if board_int in dec_dict:
            dec_moves = dec_dict[board_int]
            move_index = smart_move(dec_moves,moves[1])
        else:
            move_index = randint(0,len(moves[1])-1)
        my_move = moves[1][move_index]
        board[my_move[0][0]][my_move[0][1]] = 0
        board[my_move[1][0]][my_move[1][1]] = team
        if moves[0] == "take":
            enemy_x = int((my_move[1][0] - my_move[0][0])/2 + my_move[0][0])
            enemy_y = int((my_move[1][1] - my_move[0][1])/2 + my_move[0][1])
            board[enemy_x][enemy_y] = 0
        if team == -1 and my_move[1][0] == 0:
            board[my_move[1][0]][my_move[1][1]] = -2
        elif team == 1 and my_move[1][0] == 7:
            board[my_move[1][0]][my_move[1][1]] = 2
        return[board,my_move]
    else:
        return "loss"
    
def play_game(dec_dict_1, dec_dict_2, s_t_1, s_t_2):
    con = True
    team = -1
    board = copy.deepcopy(start_board)
    counter = 0
    while con:
        if team == -1:
            dec_dict = dec_dict_1
            state_transform = copy.copy(s_t_1)
        elif team == 1:
            dec_dict = dec_dict_2
            state_transform = copy.copy(s_t_2)
        counter += 1
        moves = find_moves(board,team)
        made_move = make_move(moves,board,team, dec_dict, state_transform)
        if made_move == "loss":
            con = False
        elif counter>100:
            con = False
            return 200
        team = team * -1
    return team

def state_getter(board,state_transform):
    state = ""
    if state_transform == 1:
        for x in board:
            count = 0
            for y in x:
                if y > 0:
                    count += 1
            state = state + str(count)
        for x in board:
            count = 0
            for y in x:
                if y < 0:
                    count += 1
            state = state + str(count)
    elif state_transform == 2:
        for i in range(8):
            count = 0
            for j in range(8):
                if board[j][i] > 0:
                    count += 1
            state = state + str(count)
        for i in range(8):
            count = 0
            for j in range(8):
                if board[j][i] < 0:
                    count += 1
            state = state + str(count)
    elif state_transform == 3:
        for i in range(4):
            count = 0
            for j in range(16):
                if board[i+j//8][j%8] > 0:
                    count += 1
            state = state + str(count)
        for i in range(4):
            count = 0
            for j in range(16):
                if board[i+j//8][j%8] < 0:
                    count += 1
            state = state + str(count)
    elif state_transform == 4:
        for i in range(4):
            count = 0
            for j in range(16):
                if board[j%8][i+j//8] > 0:
                    count += 1
            state = state + str(count)
        for i in range(4):
            count = 0
            for j in range(16):
                if board[j%8][i+j//8] < 0:
                    count += 1
            state = state + str(count)
    return state
      
def check_command():
    fail_message = ''' 
    Fail message
    '''
    try:
        p_1_1 = int(sys.argv[1][1])
        p_1_2 = int(sys.argv[1][3])
        p_2_1 = int(sys.argv[2][1])
        p_2_2 = int(sys.argv[2][3])
    except:
        print(fail_message)
        exit(1)
    con = True
    con = con and sys.argv[1][4:9] == sys.argv[2][4:9] == ".json"
    con = con and sys.argv[1][0] == sys.argv[2][0] == "s"
    con = con and sys.argv[1][2] == sys.argv[2][2] == "t"
    con = con and 0 < p_1_1 <= 10
    con = con and 0 < p_1_2 <= 10
    con = con and 0 < p_2_1 <= 10
    con = con and 0 < p_2_2 <= 10
    if not con:
        print(fail_message)
        exit(1)
    
def main(j, k):
    if j == 0:
        s_t_1 = 1
        s_t_2 = 3
    elif j == 1:
        s_t_1 = 2
        s_t_2 = 4
    file_1 = "s"+str(s_t_1)+"t"+str(k)+".json"
    file_2 = "s"+str(s_t_2)+"t"+str(k)+".json"
    f = open('/home/ec2-user/machine_learning/checkers/files/'+file_1,'r')
    dec_dict_1 = json.load(f)
    f.close()
    f = open('/home/ec2-user/machine_learning/checkers/files/'+file_2,'r')
    dec_dict_2 = json.load(f)
    f.close()
    game_results = []
    i = 0
    while i < 100:
        winner = play_game(dec_dict_1, dec_dict_2, s_t_1, s_t_2)
        if winner != 200:
            game_results.append(winner)
            i+=1 
    minus_1_w = len(list(filter(lambda x: x==-1,game_results)))
    plus_1_w = len(list(filter(lambda x: x==1,game_results)))
    print("1: "+str(s_t_1)+"  2: "+str(s_t_2)+"  iter: "+str(k))
    print("Result - 1: "+str(minus_1_w)+" 2: "+str(plus_1_w))
    return([minus_1_w,plus_1_w])

for l in range(97):
    for j in range(2):
        for k in range(10):
            round_result = main(j, k)
            f = open("/home/ec2-user/machine_learning/checkers/a1_results.csv","r")
            results = f.read().split("\n")
            f.close()
            x = results[j*10+k].split(",")
            x[0] = str(int(x[0])+round_result[0])
            x[1] = str(int(x[1])+round_result[1])
            x = ",".join(x)
            results[j*10+k] = x
            f = open("/home/ec2-user/machine_learning/checkers/a1_results.csv","w+")
            f.write("\n".join(results))
            f.close()
                    