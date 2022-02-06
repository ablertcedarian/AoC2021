#AoC 2021 4.1 
import sys

def checkboards(boards, target):
	newboards = boards.copy() 
	for n, board in enumerate(boards):
		for row in range(5):
			for col in range(5):
				if board[row][col] == target:
					newboards[n][row][col] = -1 
		if checkwin(board):
			return (newboards, board) 
	winningBoard = []
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
for num in numbersCalled:
	(accountBoards, winner) = checkboards(accountBoards, num)
	if len(winner) > 0:
		boardSum = getSum(winner) 
		print(boardSum*num) 
