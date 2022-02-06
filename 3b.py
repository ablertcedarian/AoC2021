#AoC 2021 3.2
import sys

input = []

with open('3b_Input.txt') as file:
	for line in file:
		input.append(line.rstrip())

length = len(input[0]) 

olist = input.copy() 
ocriteria = -1 
odelete = [] 
clist = input.copy()
ccriteria = -1 
cdelete = [] 

for i in range(length):
	counter1 = 0 
	counter0 = 0 
	if len(olist) > 1:
		for n in olist: 
			if n[i] == '1':
				counter1 += 1 
			else:
				counter0 += 1 
		if counter1 > counter0:
			ocriteria = '1' 
			ccriteria = '0'
		elif counter1 == counter0:
			ocriteria = '1' 
			ccriteria = '0'
		else:
			ocriteria = '0'
			ccriteria = '1'  
		for j,n in enumerate(olist):
			if n[i] != ocriteria: 
				odelete.append(j) 
	counter1 = 0 
	counter0 = 0 
	if len(clist) > 1:
		for n in clist: 		
			if n[i] == '1':
				counter1 += 1 
			else:
				counter0 += 1 
		if counter1 > counter0:
			ocriteria = '1' 
			ccriteria = '0'
		elif counter1 == counter0:
			ocriteria = '1' 
			ccriteria = '0'
		else:
			ocriteria = '0'
			ccriteria = '1'  
		for j,n in enumerate(clist):
			if n[i] != ccriteria: 
				cdelete.append(j) 
	while len(odelete) > 0:
		del olist[odelete[-1]] 
		del odelete[-1]
	while len(cdelete) > 0:
		del clist[cdelete[-1]] 
		del cdelete[-1]


print(olist, clist) 

oxy = int(olist[0], 2)
co2 = int(clist[0], 2) 

print(oxy)
print(co2)

print(oxy*co2) 
