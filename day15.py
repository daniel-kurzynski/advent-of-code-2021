import numpy as np
import timeit

def lowestRisk(puzzle):
    queue = [(0,0)]

    visited = np.zeros(puzzle.shape, dtype=bool)
    risk = np.zeros(puzzle.shape)

    def visitNext(current, next):
        if not visited[next] or risk[next]>risk[current]+puzzle[next]:
            visited[next] = True
            risk[next] = risk[current]+puzzle[next]
            queue.append(next)

    while len(queue)>0:
        current = queue.pop(0)

        if current[0]>0:
            visitNext(current, (current[0]-1, current[1]))

        if current[0]<puzzle.shape[0]-1:
            visitNext(current, (current[0]+1, current[1]))

        if current[1]>0:
            visitNext(current, (current[0], current[1]-1))

        if current[1]<puzzle.shape[1]-1:
            visitNext(current, (current[0], current[1]+1))

    return risk[-1,-1]


puzzle = np.array([
    [1,1,6,3,7,5,1,7,4,2],
    [1,3,8,1,3,7,3,6,7,2],
    [2,1,3,6,5,1,1,3,2,8],
    [3,6,9,4,9,3,1,5,6,9],
    [7,4,6,3,4,1,7,1,1,1],
    [1,3,1,9,1,2,8,1,3,7],
    [1,3,5,9,9,1,2,4,2,1],
    [3,1,2,5,4,2,1,6,3,9],
    [1,2,9,3,1,3,8,5,2,1],
    [2,3,1,1,9,4,4,5,8,1]
])

print(lowestRisk(puzzle))
