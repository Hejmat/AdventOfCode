## https://adventofcode.com/2020/day/5
seznam = []
# Define input
file = 'No5_input.txt'
with open(file,'r') as f:
    lines = f.readlines()
    for line in lines:
        seznam.append(line)
f.close()

#Part1
results = [] #List for appending seat numbers
for x in seznam:
    #Starting max and min for rows
    ma = 127
    mi = 0
    #Starting max and min for columns
    ma2 = 7
    mi2 = 0
    
    row = x[:-3] #Extract symbols defining rows in plane
    col = x[7:] #Extract symbols defining columns in plane
    for r in row:
        if r == 'F': #Continue with lower half
            ma = (ma+mi+1)/2 - 1
        if r == 'B': #Continue with upper half
            mi = (ma+mi+1)/2
    
    for c in col:
        if c == 'L':
            ma2 = (ma2+mi2+1)/2 - 1
        if c == 'R':
            mi2 = (ma2+mi2+1)/2
    
    results.append(int(ma * 8 + ma2))
#Part2
results = sorted(results)
res = [x for x in range(results[0], results[-1]+1) if x not in results][0]

print('Part1 result is:', max(results))
print('Part2 result is:', res)
