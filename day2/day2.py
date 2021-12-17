import numpy as np

def filterByCommand(commands, commandString):
    return np.array([int(command[1] if command[0]==commandString else 0) for command in commands])

with open('input.txt') as f:
    commands = np.array([x.split(" ") for x in [x.strip() for x in f.readlines()]])

    forward_commands = filterByCommand(commands, 'forward')
    up_commands = filterByCommand(commands, 'up')
    down_commands = filterByCommand(commands, 'down')
    depth_commands = down_commands-up_commands

    forward_position = sum(filterByCommand(commands, 'forward'))

    depth_position_1 = sum(depth_commands)
    print(f"Part1: Product of final position: {forward_position * depth_position_1}")

    aims = [sum(depth_commands[:i+1]) for i in range(len(depth_commands))]
    depth_position_2 =  sum(aims*forward_commands)
    print(f"Part2: Product of final position: {forward_position * depth_position_2}")