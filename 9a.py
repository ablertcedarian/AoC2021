#AoC 2021 9.1
import sys

input = []
outputs = [] 

with open('9a_Input.txt') as file:
	for line in file:
		input.append([int(a) for a in line.rstrip()])

print(input)

h = len(input)
w = len(input[0])
print("dimensions")
print(h, w)

steps = [(0,1),
		 (1,0),
		 (0,-1),
		 (-1,0)]

def findBasinSize
lows = []
for rowNum, row in enumerate(input):
	for colNum, col in enumerate(row):
		originalValue = input[rowNum][colNum]
		for (ix,jx) in steps:
			new_row = rowNum + ix
			new_col = colNum + jx 
			if new_row < 0 or new_row > h - 1:
				continue 
			elif new_col < 0 or new_col > w - 1:
				continue 
			if originalValue >= input[new_row][new_col]:
				
		else:
			lows.append(originalValue)

print(lows)
print(sum(lows)+len(lows)) 






