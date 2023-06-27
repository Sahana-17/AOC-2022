#AOC 2022 - Day 8

#Finding visible trees in a grid

#Part 1 Answer : 1823
#Part 2 Answer : 211680

import os

file_path = os.path.join(os.path.dirname('__file__'), "day8.in")

with open(file_path) as file:

    grid = [list(map(int, line.strip())) for line in file]

check_list = [0,len(grid)-1]

rows = len(grid)
columns = len(grid[0])

def part1():

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

def part2():
    max_trees = 0
   
    for i in range(rows):
        for j in range(columns):

            if i not in check_list and j not in check_list:
                right_max = float('inf')
                for k in range(j + 1, len(grid)):
                    if grid[i][k] >= grid[i][j]:
                        right_max = min(right_max, k - j)
                    else:
                        right_max = min(right_max, len(grid) - j - 1)

                left_max = float('inf')
                for k in range(j - 1, -1, -1):
                    if grid[i][k] >= grid[i][j]:
                        left_max = min(left_max, j - k)
                    else:
                        left_max = min(left_max, j)

                down_max = float('inf')
                for k in range(i + 1, len(grid)):
                    if grid[k][j] >= grid[i][j]:
                        down_max = min(down_max, k - i)
                    else:
                        down_max = min(down_max, len(grid) - i - 1)

                up_max = float('inf')
                for k in range(i - 1, -1, -1):
                    if grid[k][j] >= grid[i][j]:
                        up_max = min(up_max, i - k)
                    else:
                        up_max = min(up_max, i)

                max_trees = max(max_trees, right_max * left_max * down_max * up_max)

    return max_trees

print("Visible Trees :", part1())
print("Max Trees :", part2())