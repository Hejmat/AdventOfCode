## https://adventofcode.com/2020/day/2
seznam = []

# Define input
file = 'No2_input.txt'
with open(file,'r') as f:
    lines = f.readlines()
    for line in lines:
        seznam.append(line.replace('\n',''))
f.close()

result = 0
result2 = 0
for x in seznam:
    s = x.replace(':','').split(' ')
    count = s[2].count(s[1]) #Find letter occurrence(index 1) in password(index2)

    n = int(s[0].split('-')[0]) # Find lower threshold
    m = int(s[0].split('-')[1])
    
    ## Part 1
    if n <= int(count) <= m: # If No of occurrences is between thresholds
        result = result + 1
    
    ## Part 2
    if s[1] == s[2][n-1] or s[1] == s[2][m-1]: # If letter occur on one of the positions
        if s[2][n-1] != s[2][m-1]: # If letters on both positions aren't identical
            result2 = result2 + 1
        
print('Vysledek casti 1 je:', result)
print('Vysledek casti 2 je:', result2)
