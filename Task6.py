## https://adventofcode.com/2020/day/6
seznam = []
# Define input
file = 'No6_input.txt'
with open(file,'r') as f:
    data = f.read()
f.close()

groups = data.split('\n\n') #Split data to list of groups

result1 = 0 #Part1 result
result2 = 0 #Part2 result
for g in groups:
    members = g.split('\n') #Split group to list of members/answers
    uni = list(set(g.replace('\n',''))) #Unique elements/questions
    result1 = result1 + len(uni) #Add number of questions to result
    #Part2
    for u in uni:
        if all(u in m for m in members) == True: #If letter occur in all members
            result2 = result2 + 1
print(result1)       
print(result2)
