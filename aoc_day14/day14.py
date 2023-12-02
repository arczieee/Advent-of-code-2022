import numpy as np
import math

with open('test.txt') as f:
    input_list = [line.rstrip() for line in f]

map = np.empty((20,18),dtype=str)
map.fill(' ')

start = (0,9)
map[start] = '+'
cordList = []
maxx = 0

for tempStr in input_list:
    tempList = tempStr.split(' -> ')
    
    for element in tempList:
        cord = element.split(',')
        dx = 500 - int(cord[0])
        cord = (int(cord[1]),9-dx)

        cordList.append(cord)
            
#print(cordList)
for (x,y) in cordList:
    if x>maxx:
        maxx = x

i = 1
while i < len(cordList):
    (x,y) = cordList[i]
    (prevx,prevy) = cordList[i-1]

    if prevx==x:
        map[x,y:prevy+1] = '#'
    
    if int(prevy)==int(y):
        map[prevx:x+1,y] = '#'

    i = i+1



#print(map)
#print(cordList)

endCond = False
countUnits = 0

while endCond == False:
    countUnits = countUnits+1
    x=0
    y=9
    stuck = False

    while stuck == False:
        if map[x+1,y] == ' ':
            x=x+1
        else:
            if map[x+1,y-1] == ' ':
                y=y-1
                x=x+1
            elif map[x+1,y+1] == ' ':
                y=y+1
                x=x+1
            else:
                stuck = True
                map[x,y] = 'o'
        if x == maxx:
            stuck = True
            endCond = True
    #print('\n')
    #print(map)

print(countUnits-1)
