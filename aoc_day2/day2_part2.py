import numpy as np

input_array = np.genfromtxt('input.txt',dtype=str)

i = 0
score = 0

def checkScore(outcome,opponent):
    if outcome == 'Y':
        if opponent == 'B':
            return 2+3
        elif opponent == 'A':
            return 1+3
        elif opponent == 'C':
            return 3+3
    elif outcome == 'X':
        if opponent == 'B':
            return 1+0
        elif opponent == 'A':
            return 3+0
        elif opponent == 'C':
            return 2+0
    elif outcome == 'Z':
        if opponent == 'B':
            return 3+6
        elif opponent == 'A':
            return 2+6
        elif opponent == 'C':
            return 1+6


while i < len(input_array):
    score = score + checkScore(input_array[i,1],input_array[i,0])

    i = i + 1

print(score)
