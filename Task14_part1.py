## https://adventofcode.com/2020/day/14
file = 'No14_input.txt'
with open(file,'r') as f:
    lines = f.read()
    inp = ['mask' + e.strip() for e in lines.split('mask') if e]
f.close()

mems = [] #List for all mems values
for i in inp:
    ii = i.split('\n')
    for q in ii[1:]:
        mem = int(q.split('[')[1].split(']')[0].strip()) #Get memory values from input
        mems.append(mem)
tar = [0 for t in range(0,max(mems))] #Create target list for filling with the output values, length of the maximum mems

for i in inp:
    ii = i.split('\n')
    mask = ii[0].split('=')[1].strip()
    nums = [o for o in ii[1:]]

    for n in nums:
        mem = int(n.split('[')[1].split(']')[0].strip())
        x = int(n.split('=')[1].strip()) #Get the number value from input
        xn = '{:036b}'.format(x) #Transform integer to 36bits
        
        ml = [y for y in mask] #List of each mask position value
        xnl = [y for y in xn] #List of each input number position value
        
        z = zip(ml,xnl) # Zip mask values and input values for transformation
        new = []
        for b in z: #Mask transformations
            if b[0] == 'X' and b[1] == '0':
                new.append('0')
            elif b[0] == 'X' and b[1] == '1':
                new.append('1')
            elif b[0] == '1' and b[1] == '1':
                new.append('1')
            elif b[0] == '1' and b[1] == '0':
                new.append('1')
            elif b[0] == '0' and b[1] == '0':
                new.append('0')
            elif b[0] == '0' and b[1] == '1':
                new.append('0')    
        tar[mem-1] = int(''.join(new), 2) #Replace value in target list on the position of the actual memory value  
print('Part1 result:', sum([p for p in tar if p != 0]))
