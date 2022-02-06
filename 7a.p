#AoC 2021 7.1
import sys

input = []

with open('6a_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

rawinput = [] 

for i,n in enumerate(input):
	rawinput.append(list(map(int, n.split(","))))

print(rawinput) 

