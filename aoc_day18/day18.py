import numpy as np
from collections import defaultdict

with open('input.txt') as f:
    input_list = [line.rstrip() for line in f]

i = 0


g = defaultdict(lambda:False)



while i<len(input_list):
    tempList = input_list[i].split(",")
    tempTuple = (int(tempList[0]),int(tempList[1]),int(tempList[2]))
    g[tempTuple] = True

    i=i+1

sum = int(0)

print(g.keys())

for x,y,z in list(g.keys()):
    for dx,dy,dz in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
        tx = x-dx
        ty = y-dy
        tz = z-dz

        tempTuple = (tx,ty,tz)

        if tempTuple in g.keys():
            a=0
        else:
            sum=sum+1



print(sum)





