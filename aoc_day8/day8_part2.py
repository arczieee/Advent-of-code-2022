import numpy as np

#30373
#25512
#65332
#33549
#35390

with open('input.txt') as f:
    input_list = [line.rstrip() for line in f]

i = 0
tempStr = input_list[0]
tempList = []
while i<len(tempStr):
    tempList.append(tempStr[i])
    i = i+1

a = np.array(tempList)

i = 0
k = 1

while k<len(input_list):
    tempStr = input_list[k]
    tempList = []
    while i<len(tempStr):
        tempList.append(tempStr[i])
        i=i+1
    
    a = np.vstack((a,tempList))

    i = 0
    k = k+1

totalTrees = a.shape[0]*a.shape[1]
columns = a.shape[1]
rows = a.shape[0]
print('columns = %d'%columns)
print('rows = %d'%rows)
print(totalTrees)

isVisible = np.zeros([rows,columns],dtype=int)

#left to right
row = 1
column = 1
maxH = 0
while row < rows-1:
    maxH = a[row,0]
    while column < columns-1:
        if a[row,column]>maxH:
            isVisible[row,column] = 1
            maxH = a[row,column]      
        column = column+1
    column = 1
    row = row+1

#right to left
row = 1
column = columns-2
maxH = 0

while row < rows-1:
    maxH = a[row,(columns-1)]

    while column > 0:
        if a[row,column]>maxH:
            isVisible[row,column] = 1
            maxH = a[row,column]      
        column = column-1


    column = columns - 2
    row = row+1

#top to down
row = 1
column = 1
maxH = 0
while column < columns-1:
    maxH = a[0,column]
    while row < rows-1:
        if a[row,column]>maxH:
            isVisible[row,column] = 1
            maxH = a[row,column]      
        row = row+1
    row = 1
    column = column + 1

#down to top
column = 1
row = rows-2
maxH = 0

while column < columns-1:
    maxH = a[(rows-1),column]
    
    while row > 0:
        if a[row,column]>maxH:
            isVisible[row,column] = 1
            maxH = a[row,column]      
        row = row-1


    row = rows - 2
    column = column+1
print(isVisible)
print('\n')
j = 0
while j<columns:
    isVisible[0,j] = 1
    isVisible[rows-1,j] = 1
    isVisible[j,0] = 1
    isVisible[j,columns-1] = 1
    j = j+1

print(isVisible)

x = np.where(isVisible == 1)
print(len(x[0]))