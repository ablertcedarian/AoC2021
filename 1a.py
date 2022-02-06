#AoC 2021 1.1
import sys

input = []

with open('1a_Input.txt.txt') as file:
	for line in file:
		input.append(line.rstrip())

counterOfIncreasing = 1
lastmeasurement = input[0]

for measurement in input:
	if measurement > lastmeasurement: 
		counterOfIncreasing += 1 
	lastmeasurement = measurement 

print(counterOfIncreasing) 