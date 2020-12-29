## https://adventofcode.com/2020/day/15
file = 'No15_input.txt'
with open(file, 'r') as f:
    data = f.read()
    data = [int(d) for d in data.split(',')][::-1] #Reverse input data
f.close()
 
iterations = 2020 #Number of maximum iterations
 
while len(data) < iterations: #Loop until reach the limit of iterations
    num = data[0] #Set actual as first number in the list 
    try:
        x = data.index(num, 1) #Find index of second occurrence of actual number
    except ValueError: #Catch ValueError (if x not yet in list)
        x = 0 
    data.insert(0, x) #Insert variable x on the first position in list
 
print('Part1 result:', data[0])
