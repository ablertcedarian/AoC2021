#AoC 2021 4.2
import sys

def checkboards(boards, target):
	newboards = boards.copy() 
	for n, board in enumerate(boards):
		for row in range(5):
			for col in range(5):
				if board[row][col] == target:
					newboards[n][row][col] = -1 
	winningBoard = []
	for n, board in enumerate(boards):
		if checkwin(board):
			winningBoard.append(board) 
	return (newboards, winningBoard)

def checkwin(board):
	for row in range(5):
		if sum(board[row]) == -5:
			return True 
	for col in range(5):
		colSum = 0 
		for row in range(5):
			colSum += board[row][col] 
		if colSum == -5:
			return True 
	return False 

def getSum(board):
	total = 0 
	for row in range(5):
		for col in range(5):
			if board[row][col] != -1:
				total += board[row][col] 
	return total 

input = []

with open('4a_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

numbersCalled = [] 
boardsraw = [] 

for i,n in enumerate(input):
	if i == 0:
		numbersCalled = list(map(int, n.split(','))) 
	elif n == "":
		pass 
	else: 
		boardsraw.append(list(map(int, n.split())))

boards = []
for i,n in enumerate(boardsraw):
	if i % 5 == 0:
		boards.append([x for x in boardsraw[i:i+5]])

accountBoards = boards.copy() 

winner = []
last = ([], -1)
lastnum = -1 
for num in numbersCalled:
	(accountBoards, winner) = checkboards(accountBoards, num)
	if len(winner) > 0 and len(accountBoards) == 1: 
		lastnum = num 
		break 
	for winBoard in winner: 
		boardSum = getSum(winBoard) 
		if len(accountBoards) > 1:
			last = (winBoard, num) 
			k = accountBoards.index(winBoard)  
			del accountBoards[k]
		else:
			break 
	print(accountBoards)


print("last standing!")
print(accountBoards[0])
print(getSum(accountBoards[0])*(lastnum))
