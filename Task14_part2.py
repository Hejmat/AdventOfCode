## https://adventofcode.com/2020/day/14
import itertools
import re

file = 'No14_input.txt'
with open(file,'r') as f:
    lines = f.read()
    inp = ['mask' + e.strip() for e in lines.split('mask') if e]
f.close()

tar = [[0,0] for t in range(0,90000)] #Create target list for filling with the memory and address values

def replacenth(string, substr, repl, n): #Function for replace nth occurrence of substring with replacement string in target string
    place = [m.start() for m in re.finditer(substr, string)][n-1] #Find index of the nth occurrence
    b = string[:place] #String before the nth occurrence
    a = string[place:] #String after the nth occurrence
    a = a.replace(substr, str(repl), 1) #Replace the first occurrence in string 'after' the nth occurrence 
    string = b + a #Concatenate before string and new string
    return(string) #return new string

w =  0 #Index of current position in output list
for i in inp: #Loop for each task in input
    ii = i.split('\n') #Split task to lines
    mask = ii[0].split('=')[1].strip() #First line is mask
    nums = [o for o in ii[1:]] #All other lines

    for n in nums:
        mem = int(n.split('[')[1].split(']')[0].strip()) #Get the memory value from input
        x = int(n.split('=')[1].strip()) #Get the number from input
        xn = '{:036b}'.format(mem) #Transform integer to string of 36bits
        
        ml = [y for y in mask] #List of each mask position value
        xnl = [y for y in xn] #List of each input number position value
      
        z = zip(ml,xnl) # Zip mask values and input values for transformation
        new = []
        for b in z: #Mask transformations
            if b[0] == 'X' and b[1] == '0':
                new.append('X')
            elif b[0] == 'X' and b[1] == '1':
                new.append('X')
            elif b[0] == '1' and b[1] == '1':
                new.append('1')
            elif b[0] == '1' and b[1] == '0':
                new.append('1')
            elif b[0] == '0' and b[1] == '0':
                new.append('0')
            elif b[0] == '0' and b[1] == '1':
                new.append('1')
        c = new.count('X') #Get number of occurrence of 'X' symbol in transformed value        
        new_string = ''.join(new) #Build string from the transformed list        
        lst = list(itertools.product([0, 1], repeat=c)) #Find all combinations of 0,1 values (length of the combination is count of X occurrences in transformed value
        
        for ele in lst: #Loop for each combination
            new_string = ''.join(new) #Rebuild again string from transformed list
            for e in ele: #Loop for replacing X symbols with symbols from the actual combination
                new_string = replacenth(new_string,'X',e,0)
            tar[w][0] = int(new_string, 2) #Transform binary address to integer and append to first position of actual w index
            tar[w][1] = x #Append the value to second position of actual w index
            w = w + 1
xx = []
xxx = []                
tar.reverse() #Reverse target list to loop from the latest values
for t in tar: #Append only the latest value of the same address
    if t[0] not in xx:
        xx.append(t[0])
        xxx.append(t[1])
print('Part2 result:', sum(xxx))
