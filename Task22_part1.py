## https://adventofcode.com/2020/day/22
p1 = [47,19,22,31,24,6,10,5,1,48,46,27,8,45,16,28,33,41,42,36,50,39,30,11,17] #Player1 cards
p2 = [4,18,21,37,34,15,35,38,20,23,9,25,32,13,26,2,12,44,14,49,3,40,7,43,29] #Player2 cards

while len(p1) > 0 and len(p2) > 0:
    s = [p1[0],p2[0]] #Actuall first card of each player 
    if s[0] > s[1]: #If player 1 wins the round
        p1.pop(0) #Remove first card from deck
        p2.pop(0)
        p1.append(s[0]) #Append higher card to deck
        p1.append(s[1]) #Append lower card to deck
    if s[0] < s[1]: #If player 2 wins the round
        p1.pop(0)
        p2.pop(0)
        p2.append(s[1])
        p2.append(s[0])
#Store the winning deck into variable
if len(p1) > len(p2):
    winner = p1
else:
    winner = p2
#Create reverse list of values
w = [v for v in range(1,len(winner) + 1)] 
w.reverse()
z = list(zip(winner,w))
print('Part1 result:', sum([a[0]*a[1] for a in z]))
