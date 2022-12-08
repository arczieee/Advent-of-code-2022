#D:/python_3.8.10/python.exe day5_part2.py
import numpy as np

#input_array = np.genfromtxt('test.txt',dtype=str)

with open('input.txt') as f:
    input_list = f.readlines()

i = 0
countRows = 0
countColumns = 0

moves_start_row = 0

while i<len(input_list):
    temp_string = input_list[i]

    if temp_string[1] == '1':
        countRows = i
        moves_start_row = i+2
        countColumns = temp_string[len(temp_string)-3]

        i = len(input_list)
    
    i = i+1

arr = np.empty([int(countRows),int(countColumns)],dtype=str)

i = 0
j = 1
column = 0

while i<countRows:
    row = input_list[i]
    
    while j<len(row):
        char = row[j]
        if char == ' ':
            j=j+3
            column = column + 1
        else:
            arr[i,column] = char
            column = column+1
            j = j+3
        j = j+1
    
    column = 0
    j = 1
    i = i+1

top_row = np.zeros([1,arr.shape[1]],dtype=int)


i = arr.shape[0]-1
j = 0
while i>=0:
    while j<arr.shape[1]:
        if len(arr[i,j]) != 0:
            top_row[0,j] = i
        j = j+1
    j = 0
    i = i-1

empty_row = np.empty([1,int(countColumns)],dtype=str)

i = moves_start_row
j = 0
row_moves = []

while i<len(input_list):
    temp_string = input_list[i]
    x = temp_string.split(' ')
    row_moves.append(x[1])
    row_moves.append(x[3])
    row_moves.append(x[5])

    i = i+1


print(arr)
print(top_row)
print('\n')
i = 2
j = 0

while i<len(row_moves):

    howmany = int(row_moves[i-2])
    columnfrom = int(row_moves[i-1])-1
    columnto = int(row_moves [i])-1
    rowfrom = int(top_row[0,columnfrom])-1+howmany
    rowto = int(top_row[0,columnto])-1


    while j<howmany:
        if rowto == -1:

            arr = np.vstack((empty_row,arr))
            rowto = 0
            rowfrom = rowfrom+1
            top_row[0,columnto] = 0
            k = 0

            while k<int(countColumns):
                if k != columnto:
                    top_row[0,k] = top_row[0,k]+1
                k = k+1

        arr[rowto,columnto] = arr[rowfrom,columnfrom]
        arr[rowfrom,columnfrom] = ''
        top_row[0,columnfrom] = top_row[0,columnfrom]+1
        if top_row[0,columnto] != 0:
            top_row[0,columnto] = top_row[0,columnto]-1

        rowto = rowto-1
        rowfrom = rowfrom-1

        print(arr)
        print(top_row)
        print('\n')

        j = j+1
    
    j = 0
    i = i+3

outStr = ''

i = 0
while i<int(countColumns):
    letter = arr[(top_row[0,i]),i]
    outStr += letter

    i=i+1

print(outStr)