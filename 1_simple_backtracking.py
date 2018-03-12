# https://stackoverflow.com/questions/1697334/algorithm-for-solving-sudoku 	
import numpy as np

def fillNext(board):
	X,Y = np.where(board==0)
	if X.size!=0 and Y.size!=0:
		return X[0],Y[0]
	return -1,-1

def isCorrect(numbers):
	numbers = numbers[numbers>0].flatten()
	return np.unique(numbers).size == len(numbers)

def isValidInsertion(board,i,j,n):
	board[i][j] = n

	rowOk = isCorrect(board[i,:])
	colOk = isCorrect(board[:,j])
	x,y = 3*(i/3),3*(j/3)
	squareOk = isCorrect(board[x:x+3,y:y+3])

	board[i][j]=0
	return rowOk and colOk and squareOk

def solveBoard(board,i=0,j=0):
	i,j = fillNext(board)
	if i==-1:
		return True

	for n in range(1,10):
		if isValidInsertion(board,i,j,n):
			board[i][j] = n
			if solveBoard(board,i,j):
				return True
			board[i][j]=0
	return False

def printSudokuBoard(board):
	for i,row in enumerate(board):
		row_output = ''.join([str(x) if x!=0 else " " for x in row])
		print ('{} {} {}|'*3).format(*row_output)
		if i%3==2:
			print '-'*19

board = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
board = np.array(board)
if solveBoard(board):
	printSudokuBoard(board)
else:
	print "No solution"

