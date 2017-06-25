

def DrawBoard(size):
	for i in range(size):	
		print(" ---" * size)
		print("|   " * (size + 1))
	print(" ---" * size)
	return 

def checkDiagonalsForWinner(grid):
	if grid[1][1] != 0:
		diagonalOne = [grid[0][0], grid[1][1], grid[2][2]]
		if diagonalOne[0] == diagonalOne[1] == diagonalOne[2]:
			return ("The winner is player " + str(diagonalOne[0]))
		diagonalTwo = [grid[2][0], grid[1][1], grid[0][2]]
		if diagonalTwo[0] == diagonalTwo[1] == diagonalTwo[2]:
			return ("The winner is player " + str(diagonalTwo[0]))
	else:
		return False
def checkRowsColumnsForWinner(grid):
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


# DrawBoard(int(input("Please enter the size board you would like (2 - 18):")))