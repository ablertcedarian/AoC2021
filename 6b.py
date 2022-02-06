#AoC 2021 6.2
import sys

def sumAges (dictOfAges):
	total = 0
	for i in range(8+1):
		total = total + dictOfAges[i]
	return total 

input = []

with open('6a_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

rawinput = [] 

for i,n in enumerate(input):
	rawinput.append(list(map(int, n.split(","))))

print(rawinput) 

currentState = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for i,n in enumerate(rawinput[0]):
	currentState[n] = currentState[n] + 1

days = 256

for dayNum in range(days):
	newborn = currentState[0]
	for age in range(1,8+1):
		currentState[age-1] = currentState[age]
	currentState[8] = newborn 
	currentState[6] = currentState[6] + newborn 
	print(currentState) 
	print(dayNum+1, sumAges(currentState))


