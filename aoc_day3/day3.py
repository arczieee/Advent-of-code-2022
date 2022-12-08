#D:/python_3.8.10/python.exe day3.py
# a = 1 -----> 'a' in ASCII = 97
# a_priority = a_ASCII - 96

# A = 27 ----> 'A' in ASCII = 65
# A_priority = A_ASCII - 38

import numpy as np

input_array = np.genfromtxt('input.txt',dtype=str)

priority = 0
i = 0

while i < len(input_array):
    input_string = input_array[i]
    x1, x2 = input_string[:len(input_string)//2], input_string[len(input_string)//2:]

    j = 0
    k = 0

    while j < len(x1):
        while k < len(x2):
            if x1[j] == x2[k]:
                k = len(x2)
                
                if x1[j].isupper() == True:
                    priority = priority + ord(x1[j]) - 38
                else:
                    priority = priority + ord(x1[j]) - 96

                j = len(x1)
            k = k + 1
        k = 0
        j = j + 1

    i = i+1

print(priority)
