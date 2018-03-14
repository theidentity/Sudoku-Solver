import numpy as np

def prepareArray(puzzle_in):
	board = map(int,str(puzzle_in))
	board = np.array(board)
	board = board.reshape(-1,9)
	if board.shape != (9,9):
		return None
	return board

def checkSolution(board):
	if type(board) is not np.ndarray:
		print "Not a valid board"
		return False

	vals,counts = np.unique(board,return_counts=True)
	if np.array_equal(vals,np.arange(1,10)) and np.array_equal(counts,np.repeat(9,9)):
		return True
	return False

def printSudokuBoard(board):
	for i,row in enumerate(board):
		row_output = ''.join([str(x) if x!=0 else " " for x in row])
		print ('{} {} {}|'*3).format(*row_output)
		if i%3==2:
			print '-'*19