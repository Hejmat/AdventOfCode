## https://adventofcode.com/2020/day/9
import itertools
# Define input
file = 'No9_input.txt'
with open(file,'r') as f:
    lines = f.readlines()
    nums = [int(line) for line in lines]
f.close()

##PART1
i = 25 #Preamble to skip
while True:
    t = [bool((p[0] + p[1]) == nums[i]) for p in itertools.combinations(nums[i-25:i],2)] #return boolean values of comparisons pair addition and reference number
    
    if True not in t: #If no True value in list, print result and finish loop
        res = nums[i]
        print('Part1 result:', res)
        break    
    i = i + 1 #Continue to next reference number
    
##PART2
def sublists(xs): #Function to create all contiguous sublists
    n = len(xs)
    ind = list(range(n+1))
    for j,k in itertools.combinations(ind,2):
        yield xs[j:k]

while True:
    for a in range(2,len(nums)): #Define range to create lists from the main list of all possible lengths (start on index 3 because we need at least two previous numbers)      
        for x in list(sublists(nums[a:])):
            if len(x) > 1:
                if sum(x) == res: #If sum of sublist == result from Part1, compute result2 and break the loop
                    print('Part2 result', min(x) + max(x))
                    break
        break
    break
        
        
