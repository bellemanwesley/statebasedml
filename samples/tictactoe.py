from statebasedml import data
from random import choice
from copy import copy

def dumb_move(moves,team):
    move = random.choice(moves)
    return move

def smart_move(board,moves,team,model):
    options = []
    for x in moves:
        options.append(str(x))
    classifications = data.classify(datalist= {
        str(board): {
            "options": options,
            "desired_result": "win"
        }
    }, model=model
    )
    choice = classifications[]

def make_move(board,move,team):
    board[move[0]][move[1]] = team
    return board

def moves(board):
    moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                moves.append([i,j])
    return moves


def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return True
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return True
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True
    if board[2][0] == board[1][1] == board[0][2] != 0:
        return True
    return False
    

def dumb_play():
    starting_board = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    model = {}
    for i in range(10000):
        team = 1
        board = copy(starting_board)
        all_moves = []
        while not check_win(board):
            moves = moves(board)
            move = dumb_move(moves,team)
            board = make_move(board,move,team)
            options = []
            for x in moves:
                options.append(str(x))
            all_moves.append({
                str(board):{
                    "options": copy(options),
                    "choice": str(move),
                    "team": copy(team)
                    }})
            team = team *-1
        # the current value of team is the loser
        for x in all_moves:
            if all_moves[x]["team"] == team:
                all_moves[x]["result"] = "loss"
            else:
                all_moves[x]["result"] = "win"
            del all_moves[x]["team"]
        model = data.update(datalist=all_moves,model=model)
    return model


