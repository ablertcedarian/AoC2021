#AoC 2021 6.1 
import sys

input = []

with open('6a_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

rawinput = [] 

for i,n in enumerate(input):
	rawinput.append(list(map(int, n.split(","))))

print(rawinput) 

currentState = rawinput[0]

days = 18

for dayNum in range(days):
	for index,fish in enumerate(currentState):
		if fish == 0:
			currentState.append(8+1)
			currentState[index] = 6 
		else:
			currentState[index] = fish - 1
	print(dayNum + 1, currentState) 
