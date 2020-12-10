## https://adventofcode.com/2020/day/4
import re

# Define input
file = 'No4_input.txt'
with open(file,'r') as f:
    data = f.read()
f.close()

data = data.split('\n\n') #Make list of passports

req = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] # Required fields
col = ['amb','blu','brn','gry','grn','hzl','oth'] # Required eye colors

def sep(i): #Function to get value of attribute (for validation)
    return i.split(':')[1]

res = 0 #Part1 result
res2 = 0 #Part2 result
for x in data:
    if all(r in x for r in req) == True: # Return True if all required fields are in the record
        res = res + 1
        
        #Create sorted list of required fields with identical structure for later validation
        x = x.replace('\n',' ')
        s = x.split(' ')
        s.sort() #Sort list in alphabetical order
        if 'cid' in s[1]: # Pop the cid field (not required)
            s.pop(1)
        
        #Validation
        if 1920 <= int(sep(s[0])) <= 2002:
            if 2010 <= int(sep(s[5])) <= 2020:
                if 2020 <= int(sep(s[2])) <= 2030:
                    if ('cm' in s[4] and 150 <= int(sep(s[4])[:-2]) <= 193) or ('in' in s[4] and 59 <= int(sep(s[4])[:-2]) <= 76):                     
                        if len(sep(s[3])) == 7 and sep(s[3])[0] == '#' and bool(re.match("^[a-f0-9]*$",sep(s[3])[1:])) == True:
                            if any(c in sep(s[1]) for c in col):
                                if len(sep(s[6])) == 9 and bool(re.match("^[0-9]*$",sep(s[6]))) == True:
                                    print(s)
                                    res2 = res2 + 1
            
print('Part1 result:', res)
print('Part2 result:', res2)
