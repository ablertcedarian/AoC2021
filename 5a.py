#AoC 2021 5.1
import sys

input = []

with open('5a_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

rawcoords = [] 

for i,n in enumerate(input):
	rawcoords.append(list(n.split(" -> ")))

print(rawcoords)

tupleCoords = []
for i,n in enumerate(rawcoords):
	n1 = tuple(map(int,n[0].split(",")))
	n2 = tuple(map(int,n[1].split(",")))
	tupleCoords.append((n1,n2))
print(tupleCoords) 

pointsPassed = {}
twoPlusPassed = {}
for line in tupleCoords: 
	start = line[0]
	end   = line[1]
	if start[0] == end[0]:
		x      = start[0]
		nstart = min(start[1], end[1])
		nend   = max(start[1], end[1])
		for y in range(nstart, nend + 1):
			if (x,y) not in twoPlusPassed:
				if (x,y) in pointsPassed:
					twoPlusPassed[(x,y)] = 1 
				else:
					pointsPassed[(x,y)] = 1
	elif start[1] == end[1]: 
		y      = start[1]
		nstart = min(start[0], end[0])
		nend   = max(start[0], end[0])
		for x in range(nstart, nend + 1):
			if (x,y) not in twoPlusPassed:
				if (x,y) in pointsPassed:
					twoPlusPassed[(x,y)] = 1 
				else:
					pointsPassed[(x,y)] = 1

print(len(twoPlusPassed))