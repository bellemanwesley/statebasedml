from random import random
from random import randint
import copy
import json
import sys

#STEP 1: Define initial state and initial team
def initial_state():
    initial = [[0,0,0],[0,0,0],[0,0,0]]
    initial_team = 1
    return initial, initial_team

#STEP 2: Determine which moves you can make given state s
def find_moves(s):
    moves = []
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 0:
                moves.append([i,j])
    return moves
    
#STEP 3: Use Laplace's Law to determine which move to make
def decide_move(moves,strengths):
    selector_list = []
    for x in moves:
        move = str(move_transform(x))
        if move in strengths:
            strength = strengths[move]
        else:
            strength = [0,0]
        print(move,strength)
        selector_list.append(float(strength[0]+1)/float(strength[1]+2))
    selector_var = random()*sum(selector_list)
    selected = False
    print(selector_list)
    print(selector_var)
    for i in range(len(selector_list)):
        if selector_var < selector_list[i] and not selected:
            move = moves[i]
            selected = True
        selector_var -= selector_list[i]
    print(move)
    return move

#STEP 4: Make the move
def make_move(s, move, team):
    #Transform s and team based on the chosen move
    s[move[0]][move[1]] = team
    team = team * -1
    return s, team

#STEP 5: Determine the status of the game. If the game is over, determine the winner.
def game_status(s):
    #Return True if the game is not over
    #Return False if the game is over
    CONDITION = True
    for x in s:
        if x[0] == x[1] == x[2] != 0:
            CONDITION = False
            winner = x[0]
    for i in range(len(s[0])):
        if s[0][i] == s[1][i] == s[2][i] !=0:
            CONDITION = False
            winner = s[0][i]
    if s[0][0] == s[1][1] == s[2][2] != 0:
        CONDITION = False
        winner = s[0][0]
    if s[0][2] == s[1][1] == s[2][0] != 0:
        CONDITION = False
        winner = s[0][2]
    if CONDITION:
        return [True]
    else:
        return [False, winner]

#STEP 6: When the game is over, update the all_strengths dictionary depending on who won
def update_strengths(all_strengths,game_choices, winner):
    for x in game_choices:
        s = str(x[1])
        move = str(move_transform(x[2]))
        if s not in all_strengths:
            all_strengths[s] = {move:[0,0]}
        elif move not in all_strengths[s]:
            all_strengths[s][move] = [0,0]
        if x[0] == winner:
            all_strengths[s][move][0] += 1
        all_strengths[s][move][1] += 1
    return all_strengths        

#Helper A: Create a transformation from a move in moves to a string
def move_transform(move):
    move_t = ""
    for x in move:
        move_t += str(x)
    return int(move_t, 3)

#Helper B: Create a transformation from a state to a string
def state_transform(s):
    state = ""
    for x in s:
        for y in x:
            state += str(y+1)
    return int(state, 3)
    

def play_game(all_strengths):
    s, team = initial_state()
    con = True
    game_choices = []
    while con:
        moves = find_moves(s)
        print(moves)
        state = state_transform(s)
        if len(moves) > 0:
            if str(state) in all_strengths:
                strengths = all_strengths[str(state)]
            else:
                strengths = {}
            if team == -1:
                move = decide_move(moves, strengths)
            else:
                print(strengths)
                print("Your move")
                row = input("Row: ")
                col = input("Column: ")
                move = [int(row),int(col)]
            game_choices.append([team,state,move])
            s, team = make_move(s, move, team)
            status = game_status(s)
            for x in s:
                print(x)
            con = status[0]
        else:
            #Handle what to do if there are no moves to make
            status = ["Tie",0]
            con = False
    winner = status[1]
    print("The winner is",winner)
    return update_strengths(all_strengths, game_choices, winner)
    
def main():
    iterations = 1 #Number of times you want to play the game
    with open("files/tictactoe.json","r") as f:
        all_strengths = json.load(f)
    for i in range(iterations):
        all_strengths = play_game(all_strengths)
    with open("files/tictactoe.json","w+") as f:
        json.dump(all_strengths,f)
    
main()