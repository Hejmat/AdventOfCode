## https://adventofcode.com/2020/day/8

# Define input
file = 'No8_input.txt'
with open(file,'r') as f:
    lines = f.readlines()
    data = [line.strip() for line in lines]
f.close()

###PART1###

i = 0 #index in input
x = data[i] #position of actual condition
res = 0 #Part1 result
used = [] #used index in data (for breaking loop)

while True:
    if 'nop' in x:
        i = i + 1 #Add 1 to actual index
        x = data[i] #Change position to new index
        if i not in used:
            used.append(i)
        else:
            break
        
    if 'acc' in x:
        y = x.split(' ')[1] #Get accelerate number
        i = i + 1
        x = data[i]
        if i not in used:
            used.append(i)
        else:
            break
        res = res + int(y) #Add acc to result
    
    if 'jmp' in x:
        y = x.split(' ')[1] #Get jump number
        i = i + int(y) #Change index according to the jump
        x = data[i]
        if i not in used:
            used.append(i)
        else:
            break
        
print('Part1 result:', res)

###PART2###

p = len(data) - 1 #length of input data
res2 = 0 #Result 2


jmp = [d for d in data if 'jmp' in d] #List of jmp in input
nop = [d for d in data if 'nop' in d] #List of nop in input
ind = jmp + nop


for yn in ind:
    i = 0
    x = data[i]
    res = 0 
    used = [] 

    while True:
        if 'nop' in x:
            if i == p: #If index is the last in list -> change res to result 2 and break
                res2 = res
                break
            
            if i != p: #If index is not the last in list -> continue                
                if yn == x: #If on targeted value -> change condition to jmp
                    y = x.split(' ')[1]
                    i = i + int(y)
                    x = data[i]
                    if i not in used:
                        used.append(i)
                    else:
                        break                
                elif yn != x: #If not on targeted value continue with nop condition
                    i = i + 1
                    x = data[i]
                    if i not in used:
                        used.append(i)
                    else:
                        break
            
        if 'acc' in x:
            if i == p:
                y = x.split(' ')[1]
                res = res + int(y)
                res2 = res
                break
            
            if i != p:
                y = x.split(' ')[1]
                i = i + 1
                x = data[i]
                if i not in used:
                    used.append(i)
                else:
                    break
                res = res + int(y)
        
        if 'jmp' in x:
            if i == p:
                res2 = res
                break
            if i != p:
                if yn == x: #If on targeted value -> change condition to nop
                    i = i + 1
                    x = data[i]
                    if i not in used:
                        used.append(i)
                    else:
                        break                
                elif yn != x: #If not on targeted value continue with jmp condition
                    y = x.split(' ')[1]
                    i = i + int(y)
                    x = data[i]
                    if i not in used:
                        used.append(i)
                    else:
                        break
        
print('Part2 result:', res2)
