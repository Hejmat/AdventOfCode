## https://adventofcode.com/2020/day/16
file = 'No16_input.txt'
with open(file,'r') as f:
    data = f.read()
f.close()

nt = data.split('nearby tickets:')[1].strip().split('\n')
nearby_t = [y for x in nt for y in x.split(',')] #Nearby ticket from input

your_t = data.split('your ticket:')[1].strip().split('\n')[0].split(',') #Your ticket from input
values = data.split('your ticket:')[0].strip().split('\n')
value = [v.split(':')[1:] for v in values]
valu = [v[0].split('or') for v in value]
val = [y.strip() for x in valu for y in x] #List of all ranges from input

tar = []
for x in val: #Loop all ranges from input
    xx = x.split('-')
    for r in range(int(xx[0]),int(xx[1])+1):
        tar.append(str(r)) #Append numbers from range to list for part1

invalid_t = [int(x) for x in nearby_t if x not in tar] #Find nearby tickets which are not in tar list (invalid tickets)
print('Part1 result:', sum(invalid_t))
