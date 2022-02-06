#AoC 12.1 

def checkDone(currentPossibilities):
	for current in currentPossibilities:
		if current[-1] != "end":
			return True 
	return False 

import sys 

original = []

with open('12a_Input.txt') as file:
	for line in file:
		original.append([a for a in line.rstrip().split("-")])

print(original)
flattened = [j for sub in original for j in sub]
uniq = set(flattened)

print(uniq)

caveKey = {}
possibilities = [["start"]] 

for i in range(len(original)):
	newi = list(reversed(original[i]))
	original.append(newi) 

for connection in original:
	term0 = connection[0]
	term1 = connection[1]
	if term0 != "end" and term1 != "start":
		if term0 in caveKey:
			temp = caveKey[term0]
			if type(temp) == str:
				temp = [temp]
			temp.append(term1)
			caveKey[term0] = temp
		else:
			caveKey[term0] = term1 

print(caveKey)

notEnded = True 

while notEnded:
	toDelete = []
	for i in range(len(possibilities)):
		current = possibilities[i]
		# print("current: " + str(current))
		currentTerm = current[-1]
		currentCopy = current 

		if currentTerm != "end" and currentTerm in caveKey:
			for next in caveKey[currentTerm]:
				# print("considering " + next)
				if next.islower() and next in current:
					# print("passing") 
					if i not in toDelete: 
						toDelete.append(i)	
					pass
				else:
					copy = currentCopy.copy() 
					copy.append(next)
					if copy not in possibilities:
						possibilities.append(copy)
						if i not in toDelete: 
							toDelete.append(i)

	newDel = list(reversed(toDelete))
	for index in newDel:
		del possibilities[index]

	# print(possibilities) 
	# print("deleting")
	#clean up deadends 
	toDelete = []
	for i in range(len(possibilities)):
		current = possibilities[i]
		currentTerm = current[-1]

		if currentTerm != "end" and currentTerm not in caveKey:
			toDelete.append(i) 

	# print(toDelete)
	newDel = list(reversed(toDelete))
	for index in newDel:
		del possibilities[index] 

	#check if done
	notEnded = checkDone(possibilities)
	# print(possibilities)
	# print(" ")

print(len(possibilities))