import numpy as np

def noOfFish(initial_state, number_of_days):
    state = np.zeros(9)
    for fish_state in initial_state:
        state[fish_state] = state[fish_state]+1


    for day in range(number_of_days):
        state = np.roll(state, -1)
        state[6] = state[6]+state[8]

    return sum(state)

with open('input.txt') as f:
    initial_state = np.array([int(x) for x in  f.readline().strip().split(",")])

    print(f"Part 1: Number of fish after 80 days: {noOfFish(initial_state, 80)}")
    print(f"Part 2: Number of fish after 256 days: {noOfFish(initial_state, 256)}")




