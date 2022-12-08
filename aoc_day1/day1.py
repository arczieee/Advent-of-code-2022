import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

i = 0
calories = []
sum = 0

while i<len(lines):
    if lines[i] == '\n':
        calories.append(sum)
        sum = 0
    else:
        sum = sum + int(lines[i])

    if i == (len(lines)-1):
        calories.append(sum)

    i = i + 1


calories.sort(reverse=True)

max = calories[0] + calories[1] + calories[2]
print(max)