import numpy as np




with open('test.txt') as f:
    input_list = [line.rstrip() for line in f]

i = 0
k = 0
index = 1
sum = 0

while i < len(input_list):
    left = input_list[i]
    right = input_list[i+1]

    orderOk = True


    print(left)
    print(type(left))
    print("\n")



    if orderOk == True:
        sum = sum+index
    orderOk = True

    i=i+3
    index = index+1