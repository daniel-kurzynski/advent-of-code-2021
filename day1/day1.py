
def numberOfIncreases(puzzle):
    return sum([1 if puzzle[i+1]-puzzle[i]>0 else 0 for i in range(len(puzzle)-1)])

with open('input.txt') as f:
    puzzle_part1 = [int(x.strip()) for x in f.readlines()]
    print(f"Number of increases {numberOfIncreases(puzzle_part1)}")

    puzzle_part2 = [sum(puzzle_part1[i:i+3]) for i in range(len(puzzle_part1)-2)]
    print(f"Number of increases {numberOfIncreases(puzzle_part2)}")
