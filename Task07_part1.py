## https://adventofcode.com/2020/day/7
# Define input
file = 'No7_input.txt'
with open(file,'r') as f:
    data = f.read()
f.close()
bag_groups = data.split('.')


resultBags = []  #List for counting number of gold bags

class Bag: #Define class Bag
    def __init__(self, name): #Define parameters for objects/main bags
        self.name = name
        self.contains = [] #Sublist for bags in main bag

bags = []

def contains(st): #Function to check if bag name is in list or not
    for c in bags:
        if c.name == st:
            return(c)
    return(None)
        
      
def Proccess(br): #recursive function
    for s in br.contains:
        if s.name == 'shinygold':
            resultBags.append(br)
            return(True)
        else:
            isTrue = Proccess(s)
            if isTrue == True:
                resultBags.append(br)
                return(True)                
    return(False)

for bg in bag_groups:
    if len(bg.split('contain')) > 1:
        mainColor = bg.split('contain')[0].strip().replace('bags','').replace('bag','').replace(' ','')
        
        b = contains(mainColor)
        if b == None: #If not in bags list -> append
            b = Bag(mainColor) #Add mainCOlor to class Bag
            bags.append(b) #Append object to bags list
        
        #Create list of nested bags
        containColors = bg.split('contain')[1].strip().split(',')
        containColors = [c.strip().replace('bags','').replace('bag','')[2:].strip().replace(' ','') for c in containColors]
        
        for x in containColors: #Same as MainColor
            b1 = contains(x)
            if b1 == None:
                b1 = Bag(x)
                bags.append(b1)
            b.contains.append(b1) #Add SubColor to list of the MainColor

for x in bags:
    Proccess(x)
        
print('Part1 result:', len(list(set(resultBags))))
    
