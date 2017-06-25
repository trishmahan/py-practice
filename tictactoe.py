game = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]


# def DrawBoard(size):
# 	for i in range(size):	
# 		print(" ---" * size)
# 		print("|   " * (size + 1))
# 	print(" ---" * size)
# 	return 

def checkWinner(grid):
	#check diagonals
	if grid[1][1] != 0:
		diagonalOne = [grid[0][0], grid[1][1], grid[2][2]]
		if diagonalOne[0] == diagonalOne[1] == diagonalOne[2]:
			return ("The winner is player " + str(diagonalOne[0]))
		diagonalTwo = [grid[2][0], grid[1][1], grid[0][2]]
		if diagonalTwo[0] == diagonalTwo[1] == diagonalTwo[2]:
			return ("The winner is player " + str(diagonalTwo[0]))
	#check rows/columns
	for x in range(3):
		if grid[x][0] != 0
			row = [grid[x][0], grid[x][1], grid[x][2]]
			if row[0] == row[1] == row[2]:
				return ("The winner is player " + str(row[0]))
		if grid[0][x] != 0
			column = [grid[0][x], grid[1][x], grid[2][x]]
			if column[0] == column[1] == column[2]:
				return ("The winner is player " + str(column[0]))
	else:
		return False



print checkWinner(winner_is_2)
# DrawBoard(int(input("Please enter the size board you would like (2 - 18):")))