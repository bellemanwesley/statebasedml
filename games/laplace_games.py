from random import random
from random import randint
import copy
import json
import sys

#STEP 1: Define initial state 
def initial_state():
    initial = []
    initial_team = 1
    return initial, initial_team

#STEP 2: Determine which moves you can make given state s
def find_moves(s):
    moves = []
    return moves
    
#STEP 3: Use Laplace's Law to determine which move to make
def decide_move(moves,strengths):
    move = ""
    return move

#STEP 4: Make the move
def make_move(s, move):
    #Transform s and team based on the chosen move
    return s, team

#STEP 5: Determine the status of the game. If the game is over, determine the winner.
def game_status(s):
    #Return True if the game is not over
    #Return False if the game is over
    if CONDITION:
        return [True]
    else:
        return [False, winner]

#STEP 6: When the game is over 

#Helper A: Create a transformation from a move in moves to a string
def move_transform(move):
    pass

#Helper B: Create a transformation from a state to a string
def state_transform(s):
    pass

def play_game(all_strengths):
    s, team = initial_state()
    con = True
    game_choices = []
    while con:
        moves = find_moves(s)
        move = decide_move(moves, all_strengths[s])
        game_choices.append([team,s,move])
        s, team = make_move(s, move)
        status = game_status(s)
        con = status[0]
    winner = status[1]
    return []
    
def main():
    iterations = 10 #Number of times you want to play the game
    all_strengths = {}
    for i in range(iterations):
        play_game(all_strengths)
    

main()