import numpy as np
import math
from collections import defaultdict
import heapq as heap



with open('test.txt') as f:
    input_list = [line.rstrip() for line in f]


i = 0

while i<len(input_list):
    tempList = []
    tempList[:0] = input_list[i]

    if i == 0:
        arr = np.array(tempList)
    else:
        tempArr = np.array(tempList)
        arr = np.vstack((arr,tempArr))

    i = i+1

result = np.where(arr=="S")
temp = result[0]
row = temp[0] #starting row
temp = result[1]
column = temp[0] #starting column

result = np.where(arr=="E")
temp = result[0]
endRow = temp[0] #end row
temp = result[1]
endColumn = temp[0] #end column

i = 0
j = 0
currentVal = 'a'

moves = 0

noOfRows = arr.shape[0]
noOfColumns = arr.shape[1]




currentPos = [0,0]
stack = []
stack.append(currentPos)


dist = np.zeros((noOfRows,noOfColumns),dtype=float)
prev = np.zeros((noOfRows,noOfColumns),dtype=float)
Q = []

i = 0
j = 0

while i < noOfRows:
    while j < noOfColumns:
        dist[i,j] = np.Infinity
        prev[i,j] = 0
        Q.append([i,j])
        j +=1
    i+=1
    j=0

i = 0
j = 0
dist[i,j] = 0

print(dist)
print("\n")
print(prev)
print("\n")
print(len(Q))
print("\n")

