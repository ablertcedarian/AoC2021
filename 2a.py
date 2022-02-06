#AoC 2021 2.1 
import sys

input = []

with open('2a_Input.txt') as file:
	for line in file:
		input.append(line.rstrip().split(' '))

x = 0
y = 0

for n in input: 
	direction = n[0] 
	amount    = int(n[1])
	if direction == "forward":
		x += amount 
	elif direction == "down":
		y += amount 
	elif direction == "up":
		y -= amount 

print(x*y) 