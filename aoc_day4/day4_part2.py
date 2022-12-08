#D:/python_3.8.10/python.exe day4_part2.py
# example of input row: 2-8,3-7
# range1 = 2-8
# range2 = 3-7
# a = 2
# b = 8
# c = 3
# d = 7

import numpy as np

input_array = np.genfromtxt('input.txt',dtype=str)

i = 0
counter = 0

while i<len(input_array):
    range = input_array[i].split(',')
    range1 = range[0]
    range2 = range[1]

    range = range1.split('-')
    a = range[0]
    b = range[1]

    range = range2.split('-')
    c = range[0]
    d = range[1]

    if((int(c)>int(b))or(int(a)>int(d))):
        counter = counter + 1


    i = i+1

overlaping = len(input_array)-counter
print(overlaping)

