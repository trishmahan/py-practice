gameBoard = [[0,0,0], [0,0,0], [0,0,0]]
def DrawBoard(size, gameBoard):
	print ("    0   1   2")
	for x in range(3):
		print("   --- --- ---")
		print(str(x) + " | " + str(gameBoard[x][0]) + " | " + str(gameBoard[x][1]) + " | " + str(gameBoard[x][2]) + " |")
	print("   --- --- ---")
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
		if grid[x][0] != 0:
			row = [grid[x][0], grid[x][1], grid[x][2]]
			if row[0] == row[1] == row[2]:
				return ("The winner is player " + str(row[0]))
		if grid[0][x] != 0:
			column = [grid[0][x], grid[1][x], grid[2][x]]
			if column[0] == column[1] == column[2]:
				return ("The winner is player " + str(column[0]))
	else:
		return False	

def checkGameBoardFull(grid):
	boardSpacesFilledCount = 0
	for x in range(3):
		for y in range(3):
			if grid[x][y] != 0:
				boardSpacesFilledCount+=1
	if boardSpacesFilledCount == 9:
		return False
	else:
		return True

def updateGameBoard(location, turn):
	if turn == 1:
		marker = "X"
	elif turn == 2:
		marker = "O"
	try: 
		x,y = location.split(",")
		x = int(x)
		y = int(y)
		if gameBoard[x][y] == 0:
			gameBoard[x][y] = marker
			return "valid"
		else:
			return "invalid"
	except:
		return "invalid"

turn = 1
inputcheck = "valid"
while (not checkDiagonalsForWinner(gameBoard) and not checkRowsColumnsForWinner(gameBoard) and checkGameBoardFull(gameBoard)):
	DrawBoard(3, gameBoard)
	if turn == 1:
		if inputcheck == "valid":
			inputcheck = updateGameBoard(input("Player 1, Please enter the location you would like to place an X row,column: "), turn)
		else:
			inputcheck = updateGameBoard(input("Player 1, Last input was invalid, please enter row,column: "), turn)
		if inputcheck != "invalid":
			turn = 2
	else:
		if inputcheck == "valid":
			inputcheck = updateGameBoard(input("Player 2, Please enter the location you would like to place an O row,column: "), turn)
		else:
			inputcheck = updateGameBoard(input("Player 2, Last input was invalid, please enter row,column: "), turn)

		if inputcheck != "invalid":
			turn = 1
DrawBoard(3, gameBoard)
if checkDiagonalsForWinner(gameBoard):
	print(checkDiagonalsForWinner(gameBoard))
elif checkRowsColumnsForWinner(gameBoard): 
	print(checkRowsColumnsForWinner(gameBoard))
else:
	print("There is no winner!")