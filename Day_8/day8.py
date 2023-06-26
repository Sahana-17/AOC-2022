#AOC 2022 - Day 8

#Finding visible trees in a grid

#Part 1 Answer : 1823

import os

file_path = os.path.join(os.path.dirname('__file__'), "day8.in")

with open(file_path) as file:

    grid = [list(map(int, line.strip())) for line in file]

check_list = [0,len(grid)-1]

rows = len(grid)
columns = len(grid[0])

def check_visibility():

    visible = 0
    
    for i in range(rows):
        for j in range(columns):
 
            if i in check_list or j in check_list:
                visible += 1
            else:
                right_max = max(grid[i][j+1:])
                left_max = max(grid[i][:j])
                down_max = max(grid[k][j] for k in range(i+1, rows))
                up_max = max(grid[k][j] for k in range(0, i))
                
                if min(right_max, left_max, down_max, up_max) < grid[i][j]:
                    visible += 1

    return visible


print("Visible Trees :", check_visibility())