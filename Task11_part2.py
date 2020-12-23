## https://adventofcode.com/2020/day/11
# Define input
file = 'No11_input.txt'
with open(file,'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
f.close()

def right(c): #Def function to move in direction right
    while True:
        try:
            n = lines[x][s+c]
            c = c + 1
            if n != '.': #If symbol not empty floor, append symbol to list of visible seats and break
                nh.append(n)
                break
        except IndexError:
            break

def left(c): #Def function to move left
    while True:
        try:
            if (s-c) < 0:
                break
            n = lines[x][s-c]
            c = c + 1
            if n != '.':
                nh.append(n)
                break
        except IndexError:
            break
                        

def down(c): #Def function to move in direction down
    while True:
        try:
            n = lines[x+c][s]
            c = c + 1
            if n != '.':
                nh.append(n)
                break
        except IndexError:
            break

def up(c): #Def function to move in direction up
    while True:
        try:
            if (x-c) < 0:
                break
            n = lines[x-c][s]
            c = c + 1
            if n != '.':
                nh.append(n)
                break
        except IndexError:
            break
        
def rightdown(c,d): #Def function to move in direction right down
    while True:
        try:
            n = lines[x+c][s+d]
            c = c + 1
            d = d + 1
            if n != '.':
                nh.append(n)
                break
        except IndexError:
            break

def rightup(c,d): #Def function to move in direction right up
    while True:
        try:
            if (x-d) < 0:
                break
            n = lines[x-d][s+c]
            d = d + 1
            c = c + 1
            if n != '.':
                nh.append(n)
                break
        except IndexError:
            break

def leftdown(c,d): #Def function to move in direction left down
    while True:
        try:
            if (s-c) < 0:
                break
            n = lines[x+d][s-c]
            d = d + 1
            c = c + 1
            if n != '.':
                nh.append(n)
                break
        except IndexError:
            break

def leftup(c,d): #Def function to move in direction left up
    while True:
        try:
            if (x-d) < 0:
                break
            if (s-c) < 0:
                break
            n = lines[x-d][s-c]
            d = d + 1
            c = c + 1
            if n != '.':
                nh.append(n)
                break
        except IndexError:
            break

xi = len(lines) - 1 #number of last index in input
temp_lines = lines[:] #Make a copy of input list / edit by conditions
while True: #Do Iteration until it breaks itself
    x = 0 #line index
    for r in range(len(lines)):#Do iteration for each line in input
        if x == 0: #We are on first line of input
            for s in range(0, len(lines[0])):
                nh = []
                if s == 0: #Left upper corner
                    aa = 1 #Index for moving
                    n = '.'
                    right(aa) #Move right
                    
                    aa = 1 #Index for moving
                    n = '.'    
                    down(aa) #Move down
                    
                    aa = 1
                    bb = 1
                    n = '.'
                    rightdown(aa,bb) #Move right down
                    
                    if lines[x][s] == 'L' and '#' not in nh: #If actual seat is empty and all visible positions are not occupied
                        new = list(temp_lines[x]) #Make new string from actual line
                        new[s] = '#' #Change symbol of actual seat
                        temp_lines[x] = ''.join(new) #Replace the actual line by the changed string
                    if lines[x][s] == '#' and nh.count('#') > 4: #If actual seat is occupied and more than 4 adjacent are also occupied 
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)    
    
                elif s == len(lines[0])-1: #Right upper corner
                    aa = 1 #Index for moving left and right
                    n = '.'
                    left(aa)
                    
                    aa = 1 #Index for moving up and down
                    n = '.'    
                    down(aa) #Move in direction down                    
                    
                    aa = 1
                    bb = 1
                    n = '.'
                    leftdown(aa,bb) #Move in direction left down

                    if lines[x][s] == 'L' and '#' not in nh: #If actual seat is empty and all visible positions are not occupied
                        new = list(temp_lines[x]) #Make new string from actual line
                        new[s] = '#' #Change symbol of actual seat
                        temp_lines[x] = ''.join(new) #Replace the actual line by the changed string
                    if lines[x][s] == '#' and nh.count('#') > 4: #If actual seat is occupied and more than 4 adjacent are also occupied 
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)
                    
                else: #All other positions on line
                    aa = 1
                    n = '.'
                    right(aa)

                    aa = 1
                    n = '.'
                    left(aa)

                    aa = 1
                    n = '.'    
                    down(aa)
                                       
                    aa = 1
                    bb = 1
                    n = '.'                
                    rightdown(aa,bb)
                    
                    aa = 1
                    bb = 1
                    n = '.'                
                    leftdown(aa,bb)
                    
                    if lines[x][s] == 'L' and '#' not in nh: #If actual seat is empty and all visible positions are not occupied
                        new = list(temp_lines[x]) #Make new string from actual line
                        new[s] = '#' #Change symbol of actual seat
                        temp_lines[x] = ''.join(new) #Replace the actual line by the changed string
                    if lines[x][s] == '#' and nh.count('#') > 4: #If actual seat is occupied and more than 4 adjacent are also occupied 
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)
    
    ####################################################################################################
        if x == xi: #We are on last line of input
            for s in range(0, len(lines[0])):
                nh = []
                if s == 0: #Left down corner
                    aa = 1 #Index for moving
                    n = '.'
                    right(aa)
                    
                    aa = 1 #Index for moving
                    n = '.'
                    up(aa)    
                    
                    aa = 1
                    bb = 1
                    n = '.'
                    rightup(aa,bb)
                    
                    if lines[x][s] == 'L' and '#' not in nh: #If actual seat is empty and all visible positions are not occupied
                        new = list(temp_lines[x]) #Make new string from actual line
                        new[s] = '#' #Change symbol of actual seat
                        temp_lines[x] = ''.join(new) #Replace the actual line by the changed string
                    if lines[x][s] == '#' and nh.count('#') > 4: #If actual seat is occupied and more than 4 adjacent are also occupied 
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)    
    
                elif s == len(lines[0])-1: #Right down corner
                    aa = 1 #Index for moving left and right
                    n = '.'
                    left(aa)
                    
                    aa = 1 #Index for moving up and down
                    n = '.'    
                    up(aa)
                    
                    aa = 1
                    bb = 1
                    n = '.'
                    leftup(aa,bb)

                    if lines[x][s] == 'L' and '#' not in nh: #If actual seat is empty and all visible positions are not occupied
                        new = list(temp_lines[x]) #Make new string from actual line
                        new[s] = '#' #Change symbol of actual seat
                        temp_lines[x] = ''.join(new) #Replace the actual line by the changed string
                    if lines[x][s] == '#' and nh.count('#') > 4: #If actual seat is occupied and more than 4 adjacent are also occupied 
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)
                    
                else: #All other positions on last line
                    aa = 1 #Index for moving
                    n = '.'
                    right(aa)
                                       
                    aa = 1
                    n = '.'
                    left(aa)
                                       
                    aa = 1
                    n = '.'    
                    up(aa)
                                       
                    aa = 1
                    bb = 1
                    n = '.'                
                    rightup(aa,bb)
                    
                    aa = 1
                    bb = 1
                    n = '.'                
                    leftup(aa,bb)
                    
                    if lines[x][s] == 'L' and '#' not in nh: #If actual seat is empty and all visible positions are not occupied
                        new = list(temp_lines[x]) #Make new string from actual line
                        new[s] = '#' #Change symbol of actual seat
                        temp_lines[x] = ''.join(new) #Replace the actual line by the changed string
                    if lines[x][s] == '#' and nh.count('#') > 4: #If actual seat is occupied and more than 4 adjacent are also occupied 
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)                    
    ####################################################################################################
        elif x != 0 and x != xi: #If we are NOT on first or last line of input
            for s in range(0, len(lines[0])):
                nh = []
                if s == 0: #Left side of line
                    aa = 1 #Index for moving
                    n = '.'
                    right(aa)
                    
                    aa = 1
                    n = '.'    
                    up(aa)
                    
                    aa = 1
                    n = '.'    
                    down(aa)
                    
                    aa = 1
                    bb = 1
                    n = '.'                
                    rightup(aa,bb)
                    
                    aa = 1
                    bb = 1
                    n = '.'                
                    rightdown(aa,bb)#Move right down
                    
                    if lines[x][s] == 'L' and '#' not in nh: #If actual seat is empty and all visible positions are not occupied
                        new = list(temp_lines[x]) #Make new string from actual line
                        new[s] = '#' #Change symbol of actual seat
                        temp_lines[x] = ''.join(new) #Replace the actual line by the changed string
                    if lines[x][s] == '#' and nh.count('#') > 4: #If actual seat is occupied and more than 4 adjacent are also occupied 
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)    
    
                elif s == len(lines[0])-1: #Right side of line
                    aa = 1 #Index for moving left and right
                    n = '.'
                    left(aa)
                        
                    aa = 1 #Index for moving up and down
                    n = '.'    
                    down(aa)
                    
                    aa = 1 #Index for moving up and down
                    n = '.'    
                    up(aa)
                    
                    aa = 1
                    bb = 1
                    n = '.'                
                    leftup(aa,bb)
                    
                    aa = 1
                    bb = 1
                    n = '.'                
                    leftdown(aa,bb)
                    
                    if lines[x][s] == 'L' and '#' not in nh: #If actual seat is empty and all visible positions are not occupied
                        new = list(temp_lines[x]) #Make new string from actual line
                        new[s] = '#' #Change symbol of actual seat
                        temp_lines[x] = ''.join(new) #Replace the actual line by the changed string
                    if lines[x][s] == '#' and nh.count('#') > 4: #If actual seat is occupied and more than 4 adjacent are also occupied 
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)
                    
                else: #All other positions on last line
                    aa = 1 #Index for moving left and right
                    n = '.'
                    right(aa)
                                      
                    aa = 1 #Index for moving left and right
                    n = '.'
                    left(aa)
                                       
                    aa = 1 #Index for moving up and down
                    n = '.'    
                    up(aa)
                    
                    aa = 1 #Index for moving
                    n = '.'    
                    down(aa) #Move line down
                                          
                    aa = 1
                    bb = 1
                    n = '.'                
                    rightup(aa,bb)
                    
                    aa = 1
                    bb = 1
                    n = '.'                
                    rightdown(aa,bb) #Move right down
                    
                    aa = 1
                    bb = 1
                    n = '.'                
                    leftup(aa,bb)

                    aa = 1
                    bb = 1
                    n = '.'                
                    leftdown(aa,bb)
                    
                    if lines[x][s] == 'L' and '#' not in nh: #If actual seat is empty and all visible positions are not occupied
                        new = list(temp_lines[x]) #Make new string from actual line
                        new[s] = '#' #Change symbol of actual seat
                        temp_lines[x] = ''.join(new) #Replace the actual line by the changed string
                    if lines[x][s] == '#' and nh.count('#') > 4: #If actual seat is occupied and more than 4 adjacent are also occupied 
                        new = list(temp_lines[x])
                        new[s] = 'L'
                        temp_lines[x] = ''.join(new)                                                       
        x = x + 1            
    if lines == temp_lines: #If the lists are identical after last iteration, break the loop
        print('Part2 result:',''.join(temp_lines).count('#')) #Join all elements in output into one string and count # occurrences
        break
    if lines != temp_lines: #If there are still changes in the list, continue loop
        #print(temp_lines)
        lines = temp_lines[:] #Replace the primary list by the edited list
