blocked = set()
abyss = 0 

for line in open('input.txt'):
    x = [list(map(int, pair.split(','))) for pair in line.strip().split(' -> ')]
    for (x1,y1), (x2,y2) in zip(x,x[1:]):
        x1,x2 = sorted([x1,x2])
        y1,y2 = sorted([y1,y2])

        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                blocked.add(x+y*1j)
                abyss = max(abyss,y+1)


counter = 0
abyss +=1

print(abyss)

for i in range (300,800):
    blocked.add(i+abyss*1j)

while True:
    s = 500
    while True:
        if s in blocked:
            print(counter)
            exit(0)
        if s+1j not in blocked:
            s+=1j
            continue
        if s+1j-1 not in blocked:
            s+=1j-1
            continue
        if s+1j+1 not in blocked:
            s+=1j+1
            continue
        blocked.add(s)
        counter+=1
        break
    