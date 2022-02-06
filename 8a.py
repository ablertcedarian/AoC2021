#AoC 2021 8.1 
import sys

input = []

with open('8a_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

rawinput = [] 

for i,n in enumerate(input):
	rawinput.append(n.split("|"))

cleaned = []
for i,n in enumerate(rawinput):
	for term in n:
		cleaned.append(term.split(" "))

counter = 0
allowed = [2, 4, 3, 7]
# valid = []

for i, line in enumerate(cleaned):
	if i % 2 == 1:
		for n in line:
			if len(n) in allowed:
				counter += 1 
				# valid.append(n) 

print(counter) 

