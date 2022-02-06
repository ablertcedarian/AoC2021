#AoC 2021 2.2
import sys

input = []

with open('2b_Input.txt') as file:
	for line in file:
		input.append(line.rstrip().split(' '))

x   = 0
y   = 0
aim = 0

for n in input: 
	direction = n[0] 
	amount    = int(n[1])
	if direction == "down":
		aim += amount 
	elif direction == "up":
		aim -= amount 
	elif direction == "forward":
		x += amount 
		y += aim*amount 

print(x*y) 