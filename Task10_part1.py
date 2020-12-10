## https://adventofcode.com/2020/day/10
# Define input
file = 'No10_input.txt'
with open(file,'r') as f:
    lines = f.readlines()
    jolts = [int(line) for line in lines]
f.close()

jolts.sort() #Sort input min -> max
m = len(jolts) - 1 #Get maximum index of input data

ones = 1
threes = 1

i = 0

while True:
    if i < m:
        if jolts[i] + 1 == jolts[i+1]: #If the next number is 1 higher
            ones = ones + 1
            i = i + 1 #Go to next index
                
        elif jolts[i] + 3 == jolts[i+1]: #If the next number is 3 higher
            threes = threes + 1
            i = i + 1
 
    elif i == m: #on the maximum index break the loop
        print('Part1 result:', ones*threes) 
        break
