#AoC 11.2 
import sys 

original = []

with open('11a_Input.txt') as file:
	for line in file:
		original.append([int(a) for a in line.rstrip()])

input = original.copy()

steps = [(0,1),
		 (1,0),
		 (1,1),
		 (1,-1),
		 (0,-1),
		 (-1,0),
		 (-1,1),
		 (-1,-1)]

flashCounter = 0 
lastFlash    = 0
stages       = 300
flashDiff    = 0
simulStep    = 0
 
h = len(input)
w = len(input[0])
print(input) 

for stage in range(stages):
	#add 1 
	for rownum, row in enumerate(input):
		for colnum, col in enumerate(row):
			input[rownum][colnum] = input[rownum][colnum] + 1 

	#flashes 
	#flashed set to -1 
	while any(ele > 9 for ele in ([x for sub in input for x in sub])):
		for rownum, row in enumerate(input):
			for colnum, col in enumerate(row):
				if col > 9:
					for step in steps:
						init_x = rownum 
						init_y = colnum 
						new_x  = init_x + step[0]
						new_y  = init_y + step[1] 
						if new_x in range(h) and new_y in range(w):
							if input[new_x][new_y] != -1:
								input[new_x][new_y] = input[new_x][new_y] + 1 
					input[rownum][colnum] = -1 
					flashCounter += 1 

	for rownum, row in enumerate(input):
		for colnum, col in enumerate(row):
			if input[rownum][colnum] == -1:
				input[rownum][colnum] = 0 

	flashDiff = flashCounter - lastFlash 
	lastFlash = flashCounter 
	if flashDiff == h*w:
		simulStep = stage 
		break 
	if simulStep != 0:
		print("step")
		print(simulStep)

print(input) 
print(flashCounter) 
print(stage) 


