#AoC 2021 3.1 
import sys

input = []

with open('3a_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

length = len(input[0]) 

gamma = []

for i in range(length):
	counter1 = 0 
	for n in input: 
		if n[i] == '1':
			counter1 += 1 
	if counter1 > (len(input)/2):
		gamma.append(1)
	else:
		gamma.append(0)

gamma_rate   = 0 
epsilon_rate = 0

epsilon = []

for i,n in enumerate(gamma):
	gamma_rate += n*(2**(length-1-i))
	if n == 1:
		epsilon.append(0) 
	else:
		epsilon.append(1) 

for i,n in enumerate(epsilon):
	epsilon_rate += n*(2**(length-1-i)) 

print(gamma, gamma_rate)
print(epsilon, epsilon_rate)

print(gamma_rate*epsilon_rate) 