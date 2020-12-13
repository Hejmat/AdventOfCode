## https://adventofcode.com/2020/day/13
# Define input
file = 'No13_input.txt'
with open(file,'r') as f:
    lines = f.readlines()
    data = [line.strip() for line in lines]
f.close()

start = 0
t = int(data[0])
buses = [int(x) for x in data[1].split(',') if x != 'x']

times = []
tid = []
for b in buses:
    for x in range(t,t + b + 1):
        if x % b == 0:
            times.append(x)

print('Part1 result:', (min(times) - t) * buses[times.index((min(times)))])
