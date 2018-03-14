import numpy as np
import helpers
from simple_backtracking import solve
import timeit

puzzles = open('questions.txt').read().split('\n')
for puzzle in puzzles:
	board = helpers.prepareArray(puzzle)
	
	start_time = timeit.default_timer()
	board = solve(board)
	elapsed = timeit.default_timer() - start_time
	
	print helpers.checkSolution(board)
	print ('Solved in : {} sec').format(elapsed)