## https://adventofcode.com/2020/day/11
# Define input
file = 'No11_input.txt'
with open(file,'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
f.close()

xi = len(lines) - 1 #number of last index in input
temp_lines = lines[:] #Make a copy of input list / edit by conditions 
while True: #Do Iteration until it breaks itself
    x = 0 #line index
    for r in range(len(lines)):#Do iteration for each line in input
        if x != 0 and x != xi: #If we are NOT on first or last line of input
            for s in range(0, len(lines[0])): #Loop for each seat in actual line
                nh = [] #List for adjacent seats
                if s == 0: # FOr first seat on actual line
                    nh.extend((lines[x-1][s], lines[x-1][s+1], lines[x][s+1], lines[x+1][s+1], lines[x+1][s]))
                    if lines[x][s] == 'L' and '#' not in nh: #If actual seat is empty and all adjacent positions are not occupied
                        new = list(temp_lines[x]) #Make new string from actual line
                        new[s] = '#' #Change symbol of actual seat
                        temp_lines[x] = ''.join(new) #Replace the actual line by the changed string
                    if lines[x][s] == '#' and nh.count('#') > 3: #If actual seat is occupied and more than 3 adjacent are also occupied 
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)
                        
                elif s == len(lines[0])-1: # For last seat on actual line
                    nh.extend((lines[x-1][s], lines[x-1][s-1], lines[x][s-1], lines[x+1][s-1], lines[x+1][s]))
                    if lines[x][s] == 'L' and '#' not in nh:
                        new = list(temp_lines[x])
                        new[s] = '#'
                        temp_lines[x] = ''.join(new)
                    if lines[x][s] == '#' and nh.count('#') > 3:
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)

                else: #All other seats on line    
                    nh.extend((lines[x-1][s-1],lines[x-1][s],lines[x-1][s+1],lines[x][s+1],lines[x+1][s+1],lines[x+1][s],lines[x+1][s-1],lines[x][s-1]))
                    if lines[x][s] == 'L' and '#' not in nh:
                        new = list(temp_lines[x])
                        new[s] = '#'
                        temp_lines[x] = ''.join(new)
                    if lines[x][s] == '#' and nh.count('#') > 3:
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)
                    
        elif x == 0: #We are on first line of input
            for s in range(0, len(lines[0])):
                nh = []
                if s == 0:
                    nh.extend((lines[x][s+1], lines[x+1][s+1], lines[x+1][s]))
                    if lines[x][s] == 'L' and '#' not in nh:
                        new = list(temp_lines[x])
                        new[s] = '#'
                        temp_lines[x] = ''.join(new)
                    if lines[x][s] == '#' and nh.count('#') > 3:
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)                
    
                elif s == len(lines[0])-1:
                    nh.extend((lines[x][s-1], lines[x+1][s-1], lines[x+1][s]))
                    if lines[x][s] == 'L' and '#' not in nh:
                        new = list(temp_lines[x])
                        new[s] = '#'
                        temp_lines[x] = ''.join(new)
                    if lines[x][s] == '#' and nh.count('#') > 3:
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)                        

                else:
                    nh.extend((lines[x][s+1],lines[x+1][s+1],lines[x+1][s],lines[x+1][s-1],lines[x][s-1]))
                    if lines[x][s] == 'L' and '#' not in nh:
                        new = list(temp_lines[x])
                        new[s] = '#'
                        temp_lines[x] = ''.join(new)
                    if lines[x][s] == '#' and nh.count('#') > 3:
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)                        

        elif x == xi:                       
            for s in range(0, len(lines[0])):
                nh = [] 
                if s == 0: 
                    nh.extend((lines[x-1][s],lines[x-1][s+1],lines[x][s+1]))
                    if lines[x][s] == 'L' and '#' not in nh:
                        new = list(temp_lines[x])
                        new[s] = '#'
                        temp_lines[x] = ''.join(new)
                    if lines[x][s] == '#' and nh.count('#') > 3:
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)                    

                elif s == len(lines[0])-1: 
                    nh.extend((lines[x-1][s],lines[x-1][s-1],lines[x][s-1]))
                    if lines[x][s] == 'L' and '#' not in nh:
                        new = list(temp_lines[x])
                        new[s] = '#'
                        temp_lines[x] = ''.join(new)
                    if lines[x][s] == '#' and nh.count('#') > 3:
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)                        
                else:
                    nh.extend((lines[x-1][s-1],lines[x-1][s],lines[x-1][s+1],lines[x][s+1],lines[x][s-1]))
                    if lines[x][s] == 'L' and '#' not in nh:
                        new = list(temp_lines[x])
                        new[s] = '#'
                        temp_lines[x] = ''.join(new)
                    if lines[x][s] == '#' and nh.count('#') > 3:
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)                        

        x = x + 1 #Add one to line index/continue to next line
    if lines == temp_lines: #If the lists are identical after last iteration, break the loop
        print('Part1 result:',''.join(temp_lines).count('#')) #Join all elements in output into one string and count # occurrences
        break
    if lines != temp_lines: #If there are still changes in the list, continue loop
        lines = temp_lines[:] #Replace the primary list by the edited list
