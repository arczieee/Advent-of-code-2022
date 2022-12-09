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

score = []

i = 0
j = 0

while i < rows:
    while j < columns:
        left = 0
        right = 0
        up = 0
        down = 0
        #check left
        sameHreached = 0
        k = j-1
        while k>-1:
            if (sameHreached == 0):
                if a[i,j]>a[i,k]:
                    left = left+1
                elif a[i,j]==a[i,k]:
                    left = left+1
                    sameHreached = 1
                else:
                    left = left+1
                    k = -1
            else:
                if k>0:
                    if a[i,k]>a[i,k-1]:
                        left = left+1
                    else:
                        k = -1
            k=k-1
        #check right
        sameHreached = 0
        k = j+1
        while k<columns:
            if (sameHreached == 0):
                if a[i,j]>a[i,k]:
                    right = right+1
                elif a[i,j]==a[i,k]:
                    right = right+1
                    sameHreached = 1
                else:
                    right = right+1
                    k = columns
            else:
                if k<columns-2:
                    if a[i,k]>a[i,k+1]:
                        right = right+1
                    else:
                        k = columns
            k=k+1
        #check down
        sameHreached = 0
        k = i+1
        while k<rows:
            if (sameHreached == 0):
                if a[i,j]>a[k,j]:
                    down = down+1
                elif a[i,j]==a[k,j]:
                    down = down+1
                    sameHreached = 1
                else:
                    down = down+1
                    k = rows
            else:
                if k < rows-2:
                    if a[k,j]>a[k+1,j]:
                        down = down+1
                    else:
                        k = rows
            k=k+1
        #check up
        sameHreached = 0
        k = i-1
        while k>-1:
            if (sameHreached == 0):
                if a[i,j]>a[k,j]:
                    up = up+1
                elif a[i,j]==a[k,j]:
                    up = up+1
                    sameHreached = 1
                else:
                    up = up+1
                    k = -1
            else:
                if k > 0:
                    if a[k,j]>a[k-1,j]:
                        up = up+1
                    else:
                        k = -1
            k=k-1

        #end
        if i==3 and j ==2:
            print('%d\t%d\t%d\t%d'%(up,left,down,right))
        score.append(left*right*up*down)
        j=j+1
    
    
    j=0
    i=i+1

print(score)
print(max(score))