#D:/python_3.8.10/python.exe day3_part2.py
# a = 1 -----> 'a' in ASCII = 97
# a_priority = a_ASCII - 96

# A = 27 ----> 'A' in ASCII = 65
# A_priority = A_ASCII - 38

import numpy as np

input_array = np.genfromtxt('input.txt',dtype=str)

priority = 0
i = 2
j = 0
k = 0 
l = 0

while i < len(input_array):
    j = 0
    k = 0 
    l = 0
    x3 = input_array[i]
    x2 = input_array[i-1]
    x1 = input_array[i-2]

    while j < len(x1):
        while k < len(x2):
            if x1[j] == x2[k]:
                while l < len(x3):
                    if x2[k] == x3[l]:
                        if x1[j].isupper() == True:
                            priority = priority + ord(x1[j]) - 38
                        else:
                            priority = priority + ord(x1[j]) - 96
                        k = len(x2)
                        l = len(x3)
                        j = len(x1)
                    l = l + 1

            l = 0
            k = k + 1
        k = 0
        j = j+1

    i = i+3


print(priority)
