import numpy as np
from collections import defaultdict

with open('input.txt') as f:
    input_list = [line.rstrip() for line in f]

i = 0


g = defaultdict(lambda:False)
ok = set()

while i<len(input_list):
    tempList = input_list[i].split(",")
    tempTuple = (int(tempList[0]),int(tempList[1]),int(tempList[2]))
    g[tempTuple] = True
    ok.add(tempTuple)

    i=i+1

sum = int(0)

adj = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

def dfs(x,y,z,c):
    stack = [(x,y,z)]
    while len(stack)>0:
        x,y,z = stack.pop(-1)
        if x not in range(-5,25):
            continue
        if y not in range(-5,25):
            continue
        if z not in range(-5,25):
            continue
        if g[x,y,z] != 0:
            continue
        g[x,y,z] = c
        for dx,dy,dz in adj:
            stack.append((x+dx,y+dy,z+dz))


NC = 2
for i in range(-1,23):
    for j in range(-1,23):
        for k in range(-1,23):
            dfs(i,j,k,NC)
            if g[i,j,k] == NC:
                NC=NC+1

r = 0
for x,y,z in ok:
    for dx,dy,dz in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
        tx = x-dx
        ty = y-dy
        tz = z-dz

        if g[tx,ty,tz] == g[-4,-4,-4]:
            r+=1



print(r)





