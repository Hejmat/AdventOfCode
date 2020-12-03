## https://adventofcode.com/2020/day/3
seznam = []

# Define input
file = 'No3_input.txt'
with open(file,'r') as f:
    lines = f.readlines()
    for line in lines:
        seznam.append(line.replace('\n',''))
f.close()

a = len(seznam) #Number of lines
b = len(seznam[0]) #Length of each line

task = [1,3,5,7] #Steps
result = 1
for t in task:    
    trees = 0 #No of trees
    i = 0 #index
    for x in seznam:
        c = (a * t) / b
        x = x*(int(c)+1)
        if x[i] == '#':
            trees = trees + 1      
        i = i + t #Add step to index
    print(trees)
    result = trees * result

#Task, skip every second line, step = 1
trees = 0 
i = 0
line = 1 
for x in seznam:
    c = (a * 1) / b
    if line % 2 != 0: #Skip every second line
        x = x*(int(c)+1)
        if x[i] == '#':
            trees = trees + 1      
        i = i + 1
    line = line + 1 
print(trees)
result = trees * result

print('Result is:', result)
