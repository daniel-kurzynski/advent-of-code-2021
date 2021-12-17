import numpy as np
import time

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

def increaseBy(puzzle, add):
    return [[(element-1+add)%9+1 for element in dim] for dim in puzzle]

def fullPuzzle(originalPuzzle):
    extendedPuzzle = np.concatenate([increaseBy(originalPuzzle,x) for x in range(5)], axis=1)
    return np.concatenate([increaseBy(extendedPuzzle,x) for x in range(5)], axis=0)

with open('day15/input.txt') as f:
    puzzle_part1 = np.array([[int(y) for y in list(x.strip())] for x in f.readlines()])
    start = time.time()
    print(f"Risk Part 1: {lowestRisk(puzzle_part1)}")
    end = time.time()
    print(f"Solved in {(end-start):.2f}s")

    puzzle_part2 = fullPuzzle(puzzle_part1)
    start = time.time()
    print(f"Risk Part 2: {lowestRisk(puzzle_part2)}")
    end = time.time()
    print(f"Solved in {(end-start):.2f}s")