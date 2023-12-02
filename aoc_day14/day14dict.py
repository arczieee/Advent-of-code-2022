import numpy as np
import math
from collections import defaultdict

with open('test.txt') as f:
    input_list = [line.rstrip() for line in f]

print('input list length = %d'%len(input_list))

g = defaultdict(lambda:False)
maxx = 0
cordList = []
for tempStr in input_list:
    tempList = tempStr.split(' -> ')
    
    for element in tempList:
        cord = element.split(',')
        y = int(cord[0])
        x = int(cord[1])
        cordList.append((x,y))
        if x>maxx:
            maxx = x
        cordTuple = (x,y)
        g[cordTuple] = True

i = 1
while i<len(cordList):
    (x2,y2) = cordList[i]
    (x1,y1) = cordList[i-1]

    if x1==x2:
        leny = abs(y2-y1)
        y = max(y1,y2)

        while leny>=0:
            cordTuple = (x1,y)
            g[cordTuple] = True
            leny = leny-1
            y = y-1

    if y1==y2:
        lenx = abs(x2-x1)
        x = max(x1,x2)

        while lenx>=0:
            cordTuple = (x,y1)
            g[cordTuple] = True
            lenx = lenx-1
            x = x-1
    
    i=i+1

print(len(g.keys()))
sx = 0
sy = 500
counter = 0

while True:
    blocked = True

    for dx,dy in ((1,0),(1,-1),(1,1)):
        if g[sx+dx,sy+dy] == False:
            sx = sx+dx
            sy = sy+dy
            blocked = False
            break
    if sx == 9:
        break
    if blocked:
        counter +=1
        g[sx,sy] = True
        sx = 0
        sy = 500


print('\n')
print('Counter = %d'%counter)
print(len(g.keys()))


        

            
