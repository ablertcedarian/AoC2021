#AoC 2021 1.2
import sys

input = []

with open('1b_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

input = list(map(int, input))

counterOfIncreasing = 0 
lastSum = sum(input[:3])

for i, measurement in enumerate(input):
	if i < len(input) - 2: 
		currentSum = sum(input[i:i+3])
	if currentSum > lastSum: 
		counterOfIncreasing += 1 
	lastSum = currentSum 

print(counterOfIncreasing) 