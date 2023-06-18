#AOC 2022 - Day 10

#Total sum of six signal strengths

#Part 1 Answer : 13720

import os

file_path = os.path.join(os.path.dirname('__file__'), "day10.in")

with open(file_path) as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

cycle = 0
register = 1
strength = 0
total_sum = 0

def is_value(cycle):
    if cycle in [20, 60, 100, 140, 180, 220]:
        return True
    return False

for line in lines:
    if line.startswith("noop"):
        cycle += 1
        if is_value(cycle):
            strength = register * cycle
            total_sum += strength
    
    else:
        cycle += 1
        if is_value(cycle):
            strength = register * cycle
            total_sum += strength
        
        cycle += 1
        if is_value(cycle):
            strength = register * cycle
            total_sum += strength
        register += int(line[5:])

print("Total Strength:", total_sum)

