## https://adventofcode.com/2020/day/1
import itertools
seznam = []

file = 'No1_input.txt'
with open(file,'r') as f:
    lines = f.readlines()
    for line in lines:
        seznam.append(line.replace('\n',''))
f.close()
        
seznam2 = [int(item) for item in seznam] #str -> int

x = 2020 #Target
z = 0
for items in itertools.combinations(seznam2,3): #Input data and number of items in combination
    output = 1
    if sum(items) == x:
        for y in items:
            output = output * y
        print(output)
        z = z + 1
if z == 0:
    print('Neexistuje reseni')
