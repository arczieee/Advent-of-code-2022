import numpy as np
import math

with open('input.txt') as f:
    input_list = [line.rstrip() for line in f]

i = 1

itemList = []
testList = []
throwList = []

while i<len(input_list):
    tempStr = input_list[i]

    if "items" in tempStr:
        tempStr = tempStr[tempStr.find(":")+1:len(tempStr)]
        tempStr = tempStr.replace(" ","")
        tempStr = tempStr.split(",")
        itemList.append(tempStr)        

    if "divisible" in tempStr:
        tempStr = tempStr[tempStr.find("by")+3:len(tempStr)]
        testList.append(tempStr)

    if "true" in tempStr:
        tempStr = tempStr[tempStr.find("monkey")+7:len(tempStr)]
        tempList = []
        tempList.append(tempStr)

    if "false" in tempStr:
        tempStr = tempStr[tempStr.find("monkey")+7:len(tempStr)]
        tempList.append(tempStr)
        throwList.append(tempList)

    i+=1

#print(itemList)

counterList = [0,0,0,0,0,0,0,0]

i = 0
j = 0
k = 0

m = 3*13*2*11*19*17*5*7
print(m)

while k<10000:
    print(k)
    while i<len(itemList):
        listLen = len(itemList[i])
        while j<listLen:
            currentItem = int(itemList[i][0])

            if i == 0:
                counterList[i] = counterList[i]+1
                new = currentItem*17
                new = new%m
                #new = new/3
                new = math.floor(new)
                
                if new%3 == 0:
                    itemList[3].append(str(new))
                    itemList[i].remove(itemList[i][0])
                else:
                    itemList[6].append(str(new))
                    itemList[i].remove(itemList[i][0])

            if i == 1:
                counterList[i] = counterList[i]+1
                new = currentItem+2
                new = new%m
                #new = new/3
                new = math.floor(new)
                
                if new%13 == 0:
                    itemList[3].append(str(new))
                    itemList[i].remove(itemList[i][0])
                else:
                    itemList[0].append(str(new))
                    itemList[i].remove(itemList[i][0])

            if i == 2:
                counterList[i] = counterList[i]+1
                new = currentItem+1
                new = new%m
                #new = new/3
                new = math.floor(new)
                
                if new%2 == 0:
                    itemList[0].append(str(new))
                    itemList[i].remove(itemList[i][0])
                else:
                    itemList[1].append(str(new))
                    itemList[i].remove(itemList[i][0])

            if i == 3:
                counterList[i] = counterList[i]+1
                new = currentItem+7
                new = new%m
                #new = new/3
                new = math.floor(new)
                
                if new%11 == 0:
                    itemList[6].append(str(new))
                    itemList[i].remove(itemList[i][0])
                else:
                    itemList[7].append(str(new))
                    itemList[i].remove(itemList[i][0])

            if i == 4:
                counterList[i] = counterList[i]+1
                new = currentItem*currentItem
                new = new%m
                #new = new/3
                new = math.floor(new)
                
                if new%19 == 0:
                    itemList[2].append(str(new))
                    itemList[i].remove(itemList[i][0])
                else:
                    itemList[5].append(str(new))
                    itemList[i].remove(itemList[i][0])

            if i == 5:
                counterList[i] = counterList[i]+1
                new = currentItem+8
                new = new%m
                #new = new/3
                new = math.floor(new)
                
                if new%17 == 0:
                    itemList[2].append(str(new))
                    itemList[i].remove(itemList[i][0])
                else:
                    itemList[1].append(str(new))
                    itemList[i].remove(itemList[i][0])

            if i == 6:
                counterList[i] = counterList[i]+1
                new = currentItem*2
                new = new%m
                #new = new/3
                new = math.floor(new)
                
                if new%5 == 0:
                    itemList[4].append(str(new))
                    itemList[i].remove(itemList[i][0])
                else:
                    itemList[7].append(str(new))
                    itemList[i].remove(itemList[i][0])

            if i == 7:
                counterList[i] = counterList[i]+1
                new = currentItem+6
                new = new%m
                #new = new/3
                new = math.floor(new)
                
                if new%7 == 0:
                    itemList[4].append(str(new))
                    itemList[i].remove(itemList[i][0])
                else:
                    itemList[5].append(str(new))
                    itemList[i].remove(itemList[i][0])


            j+=1

        i+=1
        j=0
    #print(itemList)


    i = 0
    k+=1

print(counterList)
counterList.sort(reverse=True)
result = int(counterList[0])*int(counterList[1])
print(str(result))
