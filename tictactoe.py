"""
Tic Tac Toe Player
"""
import numpy as np
import math
import random

X = "X"
O = "O"
EMPTY = None

visited = set()

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
	return checkWin(board)


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
	w = winner(board)
	if(w == X):
		return 1
	elif(w == O):
		return -1
	else:
		return 0

def minimax(board):
	"""
	Returns the optimal action for the current player on the board.
	"""
	# hard-code the first move with the highest chance of winning
	corners = [(0,0),(0,2),(2,0),(2,2)]
	print("-----------------------------------")
	if (len(actions(board)) == 9):
		return random.choice(corners)
	if(player(board) == X):
		#print("Maximizing Player Turn")
		return maxVal(board)[1]
	else:
		#print("Minimizing Player Turn")
		return minVal(board)[1]

def maxVal(board, alpha=-1e99, beta=1e99, depth=0):
	"""`
	Simulates maximizing player
	"""
	if(terminal(board)):
		#print("Is terminal")
		return (utility(board),(None,None))
	v = -99
	bestAction = (-1,-1)
	for action in actions(board):
		res = result(board, action)
		actionVal = minVal(res, alpha, beta, 1)[0]
		if (depth == 0):
			print("Placing at",action,"is evalutated at",actionVal,"alpha:",alpha,"beta",beta)
		if(actionVal > v):
			v = actionVal
			bestAction = action
		alpha = max(alpha, actionVal)
		if beta <= alpha:
			print("breaking at",board)
			break
	return (v,bestAction)

def minVal(board, alpha=-1e99, beta=1e99, depth=0):
	"""
	Simulates minimizing player
	"""
	if(terminal(board)):
		print(board, utility(board))
		return (utility(board),(None, None))
	v = 99
	bestAction = (-1,-1)
	for action in actions(board):
		res = result(board, action)
		actionVal = maxVal(res, alpha, beta, 1)[0]
		if (depth == 0):
		if(actionVal < v):
			v = actionVal
			bestAction = action
		beta = max(beta, actionVal)
		if beta <= alpha:
			break
	return (v,bestAction)

#terminal logic

def checkRows(board):
	for row in board:
		if len(set(row)) == 1 and row[0] is not None:
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
