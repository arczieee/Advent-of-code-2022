#D:/python_3.8.10/python.exe day6.py
import numpy as np

char_list = []

with open('input.txt') as f:
    while 1:
        char = f.read(1)
        if not char:
            break

        char_list.append(char)

i = 13
j = 0
while i<len(char_list):
    checkStr = ''
    while j<14:
        checkStr += char_list[i-j]
        j = j+1

    uniqueStr = list(set(checkStr))

    if len(uniqueStr) == 14:
        print(i+1)
        i = len(char_list)

    j = 0
    i = i+1
