## https://adventofcode.com/2020/day/3
## Change numbers according to step right on lines 16,26
## Use lines 20,22,27 when u have to skip every second line
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
c = (a * 3) / b #Number to multiple line to avoid Index error, change the number according to the 'move right'

trees = 0 #No of trees
i = 0 #index
#line = 1 # Use when the task is to skip every second line
for x in seznam:
    #if line % 2 != 0: # Use when the task is to skip every second line
        x = x*(int(c)+1)
        if x[i] == '#':
            trees = trees + 1      
        i = i + 3 # change the number according to the 'move right'
    #line = line + 1 # Use when the task is to skip every second line

print('Result is:', trees)
