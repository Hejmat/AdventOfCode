## https://adventofcode.com/2020/day/12
# Define input
file = 'No12_input.txt'
with open(file,'r') as f:
    lines = f.readlines()
    data = [line.strip() for line in lines]
f.close()

##PART1
d = 'E'
r = 0
u = 0

for x in data:    
    if d == 'E':
        if x[0] == 'F':
            r = r + int(x[1:])
        elif x[0] == 'R':
            if int(x[1:]) == 90:
                d = 'S'
            elif int(x[1:]) == 180:
                d = 'W'
            elif int(x[1:]) == 270:
                d = 'N'  
        elif x[0] == 'L':
            if int(x[1:]) == 90:
                d = 'N'
            if int(x[1:]) == 180:
                d = 'W'
            if int(x[1:]) == 270:
                d = 'S'
        elif x[0] == 'N':
            u = u + int(x[1:])
        elif x[0] == 'S':
            u = u - int(x[1:])
        elif x[0] == 'W':
            r = r - int(x[1:])
        elif x[0] == 'E':
            r = r + int(x[1:])
            
    elif d == 'W':
        if x[0] == 'F':
            r = r - int(x[1:])
        elif x[0] == 'R':
            if int(x[1:]) == 90:
                d = 'N'
            elif int(x[1:]) == 180:
                d = 'E'
            elif int(x[1:]) == 270:
                d = 'S'  
        elif x[0] == 'L':
            if int(x[1:]) == 90:
                d = 'S'
            elif int(x[1:]) == 180:
                d = 'E'
            elif int(x[1:]) == 270:
                d = 'N'
        elif x[0] == 'N':
            u = u + int(x[1:])
        elif x[0] == 'S':
            u = u - int(x[1:])
        elif x[0] == 'E':
            r = r + int(x[1:])
        elif x[0] == 'W':
            r = r - int(x[1:])

    elif d == 'S':
        if x[0] == 'F':
            u = u - int(x[1:])
        elif x[0] == 'R':
            if int(x[1:]) == 90:
                d = 'W'
            elif int(x[1:]) == 180:
                d = 'N'
            elif int(x[1:]) == 270:
                d = 'E'  
        elif x[0] == 'L':
            if int(x[1:]) == 90:
                d = 'E'
            elif int(x[1:]) == 180:
                d = 'N'
            elif int(x[1:]) == 270:
                d = 'W'
        elif x[0] == 'N':
            u = u + int(x[1:])
        elif x[0] == 'E':
            r = r + int(x[1:])
        elif x[0] == 'W':
            r = r - int(x[1:])
        elif x[0] == 'S':
            u = u - int(x[1:])
            
    elif d == 'N':
        if x[0] == 'F':
            u = u + int(x[1:])
        elif x[0] == 'R':
            if int(x[1:]) == 90:
                d = 'E'
            elif int(x[1:]) == 180:
                d = 'S'
            elif int(x[1:]) == 270:
                d = 'W'  
        elif x[0] == 'L':
            if int(x[1:]) == 90:
                d = 'W'
            elif int(x[1:]) == 180:
                d = 'S'
            elif int(x[1:]) == 270:
                d = 'E'
        elif x[0] == 'S':
            u = u - int(x[1:])
        elif x[0] == 'E':
            r = r + int(x[1:])
        elif x[0] == 'W':
            r = r - int(x[1:])
        elif x[0] == 'N':
            u = u + int(x[1:])
                               
print('Part1 result:', abs(r) + abs(u))

##PART2
r = 0
u = 0

wx = 'E'
wxr = 10
wy = 'N'
wyu = 1

for x in data:    
    if x[0] == 'R':
        if int(x[1:]) == 90:
            if wx == 'E' and wy == 'N':
                wx = 'S'
                wy = 'E'
            elif wx == 'S' and wy == 'E':
                wx = 'W'
                wy = 'S'
            elif wx == 'W' and wy == 'S':
                wx = 'N'
                wy = 'W'
            elif wx == 'N' and wy == 'W':
                wx = 'E'
                wy = 'N'
        elif int(x[1:]) == 180:
            if wx == 'E' and wy == 'N':
                wx = 'W'
                wy = 'S'
            elif wx == 'S' and wy == 'E':
                wx = 'N'
                wy = 'W'
            elif wx == 'W' and wy == 'S':
                wx = 'E'
                wy = 'N'
            elif wx == 'N' and wy == 'W':
                wx = 'S'
                wy = 'E'
        elif int(x[1:]) == 270:
            if wx == 'E' and wy == 'N':
                wx = 'N'
                wy = 'W'
            elif wx == 'S' and wy == 'E':
                wx = 'E'
                wy = 'N'
            elif wx == 'W' and wy == 'S':
                wx = 'S'
                wy = 'E'
            elif wx == 'N' and wy == 'W':
                wx = 'W'
                wy = 'S'
                
    elif x[0] == 'L':
        if int(x[1:]) == 90:
            if wx == 'E' and wy == 'N':
                wx = 'N'
                wy = 'W'
            elif wx == 'S' and wy == 'E':
                wx = 'E'
                wy = 'N'
            elif wx == 'W' and wy == 'S':
                wx = 'S'
                wy = 'E'
            elif wx == 'N' and wy == 'W':
                wx = 'W'
                wy = 'S'
        elif int(x[1:]) == 180:
            if wx == 'E' and wy == 'N':
                wx = 'W'
                wy = 'S'
            elif wx == 'S' and wy == 'E':
                wx = 'N'
                wy = 'W'
            elif wx == 'W' and wy == 'S':
                wx = 'E'
                wy = 'N'
            elif wx == 'N' and wy == 'W':
                wx = 'S'
                wy = 'E'
        elif int(x[1:]) == 270:
            if wx == 'E' and wy == 'N':
                wx = 'S'
                wy = 'E'
            elif wx == 'S' and wy == 'E':
                wx = 'W'
                wy = 'S'
            elif wx == 'W' and wy == 'S':
                wx = 'N'
                wy = 'W'
            elif wx == 'N' and wy == 'W':
                wx = 'E'
                wy = 'N'        
    
    elif x[0] == 'F':
        if wx == 'E':
            r = r + (int(x[1:]) * wxr)
        if wx == 'W':
            r = r - (int(x[1:]) * wxr)
        if wx == 'N':
            u = u + (int(x[1:]) * wxr)
        if wx == 'S':
            u = u - (int(x[1:]) * wxr)
        if wy == 'E':
            r = r + (int(x[1:]) * wyu)
        if wy == 'W':
            r = r - (int(x[1:]) * wyu)
        if wy == 'N':
            u = u + (int(x[1:]) * wyu)
        if wy == 'S':
            u = u - (int(x[1:]) * wyu)
    
    elif x[0] == 'E':
        if wx == 'E':
            wxr = wxr + int(x[1:])
        elif wy == 'E':
            wyu = wyu + int(x[1:])
        elif wx == 'W':
            wxr = wxr - int(x[1:])
        elif wy == 'W':
            wyu = wyu - int(x[1:])
                        
    elif x[0] == 'W':
        if wx == 'W':
            wxr = wxr + int(x[1:])
        elif wy == 'W':
            wyu = wyu + int(x[1:])          
        elif wx == 'E':
            wxr = wxr - int(x[1:])
        elif wy == 'E':
            wyu = wyu - int(x[1:]) 
            
    elif x[0] == 'N':
        if wx == 'N':
            wxr = wxr + int(x[1:])
        elif wy == 'N':
            wyu = wyu + int(x[1:])
        elif wx == 'S':
            wxr = wxr - int(x[1:])
        elif wy == 'S':
            wyu = wyu - int(x[1:])            
                      
    elif x[0] == 'S':
        if wx == 'S':
            wxr = wxr + int(x[1:])
        elif wy == 'S':
            wyu = wyu + int(x[1:])
        elif wx == 'N':
            wxr = wxr - int(x[1:])
        elif wy == 'N':
            wyu = wyu - int(x[1:])            
            
print('Part2 result:', abs(r) + abs(u))                    
