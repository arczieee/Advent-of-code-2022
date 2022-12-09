import numpy as np
import math

#R 4
#U 4
#L 3
#D 1
#R 4
#D 1
#L 5
#R 2

with open('input.txt') as f:
    input_list = [line.rstrip() for line in f]

hx = 0
hy = 0
tx = 0
ty = 0

i = 0

rows = 0
columns = 0

while i<len(input_list):
    temp_str = input_list[i]
    x = temp_str.split(' ')

    if x[0] == 'R':
        hy = hy + int(x[1])
    elif x[0] == 'U':
        hx = hx + int(x[1])
    elif x[0] == 'L':
        hy = hy - int(x[1])
    elif x[0] == 'D':
        hx = hx - int(x[1])

    if hy>columns:
        columns = hy

    if hx>rows:
        rows = hx
    i = i+1

map = np.zeros((2000,2000),dtype=str)
tail = np.zeros((2000,2000),dtype=str)
tail[500,500] = '#'

map[500,500] = 'H'


hx = 500
hy = 500
tx = 500
ty = 500



i = 0
while i<len(input_list):
    temp_str = input_list[i]
    x = temp_str.split(' ')
    print(temp_str)
    if x[0] == 'R':
        k = 0
        while k<int(x[1]):
            hy = hy+1
            map[hx,hy] = 'H'
            map[hx,hy-1] = ''

            distance = math.sqrt(math.pow((hx-tx),2) + math.pow((hy-ty),2))

            if distance == 2:
                if hx>tx:
                    tx = tx+1
                elif hx<tx:
                    tx = tx-1
                elif hy>ty:
                    ty = ty+1
                elif hy<ty:
                    ty = ty-1
            deltax = hx-tx
            deltay = hy-ty
            if distance > 2:
                if (deltax>0)and(deltay>0):
                    tx=tx+1
                    ty=ty+1
                if (deltax>0)and(deltay<0):
                    tx=tx+1
                    ty=ty-1
                if (deltax<0)and(deltay>0):
                    tx=tx-1
                    ty=ty+1
                if (deltax<0)and(deltay<0):
                    tx=tx-1
                    ty=ty-1
            tail[tx,ty] = '#'
            k=k+1

    elif x[0] == 'U':
        k = 0
        while k<int(x[1]):
            hx = hx-1
            map[hx,hy] = 'H'
            map[hx+1,hy] = ''
            distance = math.sqrt(math.pow((hx-tx),2) + math.pow((hy-ty),2))

            if distance == 2:
                if hx>tx:
                    tx = tx+1
                elif hx<tx:
                    tx = tx-1
                elif hy>ty:
                    ty = ty+1
                elif hy<ty:
                    ty = ty-1
            deltax = hx-tx
            deltay = hy-ty
            if distance > 2:
                if (deltax>0)and(deltay>0):
                    tx=tx+1
                    ty=ty+1
                if (deltax>0)and(deltay<0):
                    tx=tx+1
                    ty=ty-1
                if (deltax<0)and(deltay>0):
                    tx=tx-1
                    ty=ty+1
                if (deltax<0)and(deltay<0):
                    tx=tx-1
                    ty=ty-1
            tail[tx,ty] = '#'
            k=k+1

    elif x[0] == 'L':
        k = 0
        while k<int(x[1]):
            hy = hy-1
            map[hx,hy] = 'H'
            map[hx,hy+1] = ''
            distance = math.sqrt(math.pow((hx-tx),2) + math.pow((hy-ty),2))

            if distance == 2:
                if hx>tx:
                    tx = tx+1
                elif hx<tx:
                    tx = tx-1
                elif hy>ty:
                    ty = ty+1
                elif hy<ty:
                    ty = ty-1
            deltax = hx-tx
            deltay = hy-ty
            if distance > 2:
                if (deltax>0)and(deltay>0):
                    tx=tx+1
                    ty=ty+1
                if (deltax>0)and(deltay<0):
                    tx=tx+1
                    ty=ty-1
                if (deltax<0)and(deltay>0):
                    tx=tx-1
                    ty=ty+1
                if (deltax<0)and(deltay<0):
                    tx=tx-1
                    ty=ty-1
            tail[tx,ty] = '#'
            k=k+1      

    elif x[0] == 'D':
        k = 0
        while k<int(x[1]):
            hx = hx+1
            map[hx,hy] = 'H'
            map[hx-1,hy] = ''
            distance = math.sqrt(math.pow((hx-tx),2) + math.pow((hy-ty),2))

            if distance == 2:
                if hx>tx:
                    tx = tx+1
                elif hx<tx:
                    tx = tx-1
                elif hy>ty:
                    ty = ty+1
                elif hy<ty:
                    ty = ty-1
            deltax = hx-tx
            deltay = hy-ty
            if distance > 2:
                if (deltax>0)and(deltay>0):
                    tx=tx+1
                    ty=ty+1
                if (deltax>0)and(deltay<0):
                    tx=tx+1
                    ty=ty-1
                if (deltax<0)and(deltay>0):
                    tx=tx-1
                    ty=ty+1
                if (deltax<0)and(deltay<0):
                    tx=tx-1
                    ty=ty-1
            tail[tx,ty] = '#'
            k=k+1

    
    i = i+1

print('\nTail:')
print(tail)
count = np.count_nonzero(tail == '#')
print('\nCells visisted = %d'%count)
#R 4
#U 4
#L 3
#D 1
#R 4
#D 1
#L 5
#R 2