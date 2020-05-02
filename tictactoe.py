"""
Tic Tac Toe Player
"""
import numpy as np
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
	"""
	Returns starting state of the board.
	"""
	return [[EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY]]

def player(board):
	"""
	Returns player who has the next turn on a board.
	"""
	count = 0
	for x in board:
		for y in x:
			if y is not None:
				count+=1
	if(count%2 == 0):
		return X
	else:
		return O
	#raise NotImplementedError


def actions(board):
	"""
	Returns set of all possible actions (i, j) available on the board.
	"""
	possibleCoords = set()
	for x in range(3):
		for y in range(3):
			if(board[x][y] is None):
				possibleCoords.add((x,y))
	return list(possibleCoords)


def result(board, action):
	"""
	Returns the board that results from making move (i, j) on the board.
	"""
	board_copy = np.copy(board).tolist()
	board_copy[action[0]][action[1]] = str(player(board))
	return board_copy

def winner(board):
	"""
	Returns the winner of the game, if there is one.
	"""
	if(checkWin(board) != 0):
		return checkWin(board)
	return 0


def terminal(board):
	"""
	Returns True if game is over, False otherwise.
	"""
	if(actions(board) == []):
		return True
	else:	
		return bool(checkWin(board))
	return False


def utility(board):
	"""
	Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
	"""
	if(winner(board) == X):
		return 1
	elif(winner(board) == O):
		return -1
	else:
		return 0

def minimax(board):
	"""
	Returns the optimal action for the current player on the board.
	"""
	if(player(board) == X):
		#print("Maximizing Player Turn")
		return maxVal(board)[1]
	else:
		#print("Minimizing Player Turn")
		return minVal(board)[1]

def maxVal(board):
	"""
	Simulates maximizing player
	"""
	if(terminal(board)):
		#print("Is terminal")
		return (utility(board),(None,None))
	v = -99
	bestAction = (-1,-1)
	for action in actions(board):
		 actionVal = minVal(result(board,action))[0]
		 if(actionVal > v):
		 	v = actionVal
		 	bestAction = action
	return (v,bestAction)

def minVal(board):
	"""
	Simulates minimizing player
	"""
	if(terminal(board)):
		#print("Is terminal")
		return (utility(board),(None, None))
	v = 99
	bestAction = (0,0)
	for action in actions(board):
		actionVal = maxVal(result(board,action))[0]
		if(actionVal < v):
			v = actionVal
			bestAction = action
	return (v,bestAction)

#terminal logic

def checkRows(board):
	for row in board:
		if len(set(row)) == 1:
			return row[0]
	return None

def checkDiagonals(board):
	if len(set([board[i][i] for i in range(len(board))])) == 1:
		return board[0][0]
	if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
		return board[0][len(board)-1]
	return None

def checkWin(board):
	#transposition to check rows, then columns
	for newBoard in [board, np.transpose(board)]:
		result = checkRows(newBoard)
		if result:
			return result
	return checkDiagonals(board)

arr = [[X, O, O],
			[O, X, X],
			[X, X, O]]
print(terminal(arr))
print(minimax(arr))
