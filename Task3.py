## https://adventofcode.com/2020/day/3
seznam = []

# Define input
file = r'c:\Users\Matous.Matous\Desktop\Prace\IBS\AdventOfCode\No3_input.txt'
with open(file,'r') as f:
    lines = f.readlines()
    for line in lines:
        seznam.append(line.replace('\n',''))
f.close()

a = len(seznam) #Number of lines
b = len(seznam[0]) #Length of each line

right = [1,3,5,7,1] #Steps right
down = [1,1,1,1,2] #Steps down
zipped = list(zip(right,down)) #Zip steps

result = 1
for z in zipped:
    trees = 0 #No of trees
    i = 0 #index
    for x in seznam[::z[1]]:
        c = (a * z[0]) / b
        x = x*(int(c)+1)
        if x[i] == '#':
            trees = trees + 1
        i = i + z[0] #Add step to index    
    print(trees)
    result = trees * result


print('Result is:', result)
