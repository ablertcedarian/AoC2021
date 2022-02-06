#AoC 2021 8.2
import sys

def processWord(letters, trans):
	print(list(letters))
	value = [0,0,0,0] 
	for letter in list(letters):
		if letter in truea:
			value[0] = 1
		elif letter in truecf:
			value[1] += 0.5 
		elif letter in truebd:
			value[2] += 0.5
		elif letter in trueeg:
			value[3] += 0.5 
		# print(letter, value)
	for index,num in enumerate(value):
		if num == 1.0:
			value[index] == 1 
	valueStr = tuple(value)
	print(trans[valueStr])
	return (trans[valueStr])

trans = {} 
trans[(1, 1, 0.5, 1)] = 0
trans[(0, 1, 0, 0)]   = 1
trans[(1, 0.5, 0.5, 1)] = 2
trans[(1, 1, 0.5, 0.5)] = 3
trans[(0, 1, 1, 0)] = 4
trans[(1, 0.5, 1, 0.5)] = 5
trans[(1, 0.5, 1, 1)] = 6
trans[(1, 1, 0, 0)]= 7
trans[(1, 1, 1, 1)] = 8 
trans[(1, 1, 1, 0.5)] = 9 

input = []
outputs = [] 

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

for i, line in enumerate(cleaned):
	if i % 2 == 0:
		print("generating")
		counter = 0
		allowed = [2, 3, 4, 7]
		valid = []
		accounted = []
		for n in line:
			if len(n) in allowed:
				counter += 1 
				if len(n) not in accounted: 
					valid.append(n) 
					accounted.append(len(n))

		true1 = []
		true4 = []
		true7 = [] 
		true8 = []

		for term in valid:
			if len(term) == 2:
				true1 = list(term)
			elif len(term) == 3:
				true7 = list(term)
			elif len(term) == 4:
				true4 = list(term)
			else:
				true8 = list(term) 
		print("values")
		print(valid)
		print(true1, true7, true4, true8)

		truea = []
		truecf = []
		truebd = []
		trueeg = []

		#find a 
		for j in true7:
			if j not in true1:
				truea = [j]
		#find cf
		for j in true7:
			if j in true1:
				truecf.append(j) 
		#find bd
		for j in true4:
			if j not in true1:
				truebd.append(j)  
		#find eg
		for j in true8:
			if j not in truea and j not in truecf and j not in truebd:
				trueeg.append(j)

		print("a")
		print(truea)
		print("cf")
		print(truecf)
		print("bd")
		print(truebd)
		print("eg")
		print(trueeg)

	if i % 2 == 1:
		print("building") 
		building = []
		for word in line:
			if word != '':
				building.append(processWord(word, trans))
		print(building) 
		finalNum = 0 
		for j,n in enumerate(building):
			finalNum += n*10**(3-j)
		print(finalNum)
		outputs.append(finalNum)

print(sum(outputs))

