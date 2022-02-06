#AoC 2021 7.1
import sys

input = []

with open('7a_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

rawinput = [] 

for i,n in enumerate(input):
	rawinput.append(list(map(int, n.split(","))))

initialPositions = rawinput[0]
start = min(initialPositions)
end   = max(initialPositions) 
# floatAvg = sum(initialPositions)/len(initialPositions)
# avg = round(floatAvg) 


possList = [[abs(x-k) for x in initialPositions] for k in range(start, end+1)]
fuelList = list(map(sum, possList))
print(min(fuelList))

