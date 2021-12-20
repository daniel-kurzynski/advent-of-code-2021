import numpy as np

def sign(x): return 1 if x > 0 else -1 if x < 0 else 0

def numberOfOverlaps(lines, ignoreDiagonal=True):
    map = np.zeros((x_max+1, y_max+1), dtype=int)

    for line in lines:

        if line[0]==line[2]:
            x = line[0]
            for y in range(min(line[1], line[3]), max(line[1], line[3])+1):
                map[y,x] = map[y,x] + 1

        elif line[1]==line[3]:
            y = line[1]
            for x in range(min(line[0], line[2]), max(line[0], line[2])+1):
                map[y,x] = map[y,x] + 1
        elif abs(line[3]-line[1]) == abs(line[2]-line[0]) and not ignoreDiagonal:
            for dif in range(0,abs(line[3]-line[1])+1):
                x = line[0] + dif * sign(line[2]-line[0])
                y = line[1] + dif * sign(line[3]-line[1])
                map[y,x] = map[y,x] + 1

    return len(map[map>1])

with open('input.txt') as f:
    lines = np.array([[int(y) for y in x.strip().replace(" -> ", ",").split(",")] for x in f.readlines()])
    x_max = np.amax([lines[:,0],lines[:,2]])
    y_max = np.amax([lines[:,1],lines[:,3]])

    print(f"Part 1: Number of overlaps: {numberOfOverlaps(lines)}")
    print(f"Part 2: Number of overlaps: {numberOfOverlaps(lines, ignoreDiagonal=False)}")




