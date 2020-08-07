from random import random
from random import randint
import copy
import json
import sys

#STEP 1: Define initial state 
def initial_state():
    initial = []
    return initial

#STEP 2: Determine which moves you can make given state s
def find_moves(s):
    moves = []
    return moves
    
#STEP 3: Use Laplace's Law to determine which move to make
def decide_move(moves,strengths):
    pass

#STEP 4: Make the move
def make_move(s, moves):
    #Transform s based on the chosen move
    return s

#STEP 5: Determine the status of the game
def game_status(s):
    #Return True if the game is not over
    #Return False if the game is over
    if CONDITION:
        return True
    else:
        return False

#STEP 6:


def play_game():
    s = initial_state()
    con = True
    while con:
        moves = find_moves(s)
    
    
def main():
    iterations = 10 #Number of times you want to play the game
    for i in range(iterations):
        play_game()
    

main()