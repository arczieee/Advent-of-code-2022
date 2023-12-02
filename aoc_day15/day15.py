import numpy as np
import math
from collections import defaultdict

sensor = set()
beacon = set()
free = set()

minx = 0
maxx = 0

with open('test.txt') as f:
    input_list = [line.rstrip() for line in f]
    for line in input_list:
        tempList = line.split('=')

        tempString = tempList[1].split(',')
        xs = int(tempString[0])

        tempString = tempList[2].split(':')
        ys = int(tempString[0])
        
        sens = xs + ys*1j

        tempString = tempList[3].split(',')
        xb = int(tempString[0])

        tempString = tempList[4]
        yb = int(tempString)

        beac = xb + +yb*1j

        minx = min(minx,xb,xs)
        maxx = max(maxx,xb,xs)

        distance = abs(xs-xb) + abs(ys-yb)
        print('Sensor = (%d,%d) Beacon = (%d,%d)'%(xs,ys,xb,yb))
        print('Distance = %d'%distance)

        sensor.add(sens)
        beacon.add(beac)

        x = xs
        y = ys
        

        for (dx,dy) in range(distance):
            x = xs+dx
            y = ys+dy
            print(x,y)
            newdistance = abs(xs-x) + abs(ys-y)

            if newdistance>distance:
                break
            else:
                free.add(x+y*1j)


print(free)


counter = 0

i = minx
while i<maxx+1:
    check = i + 10j

    if check in free:
        p = 0
    else:
        counter +=1

    i+=1

print(counter)