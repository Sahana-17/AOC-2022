#AOC 2022 - Day 12

#Dijkstra to find lowest possible path

#Part 1 Answer : 490
#Part 2 Answer : 488

import os
import pprint
from collections import deque

moves_arr = []
todo = deque()

def find_coords(grid, val):
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == val:
                
                return (i,j)         

def get_neighbours(x,y):
    neighbours = []
    for (i,j) in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
    
        if 0<=i<rows and 0<=j<columns and (ord(grid[i][j]) - ord(grid[x][y])) <= 1:
            neighbours.append((i,j))

    return neighbours


def get_shortest_path():
    visited = set()

    while todo:
        x,y, moves= todo.popleft()

        if (x,y) in visited:
            continue

        visited.add((x,y))

        if (x,y) == (endx,endy):
            return moves
        
        for (i,j) in get_neighbours(x,y):
            if ((i,j, moves+1)) not in todo:
                todo.append((i,j, moves+1))

def move_next(x,y,moves):

    if grid[x][y] == 'E':
        moves_arr.append(moves)
        return
  
    for (i,j) in get_neighbours(x,y):     
        move_next(i,j,moves+1)            
        

file_path = os.path.join(os.path.dirname('__file__'), "day12.in")

with open(file_path) as file:

    grid = [list(line.strip()) for line in file]



rows = len(grid)
columns = len(grid[0])
(startx,starty) = find_coords(grid,'S')
(endx,endy) = find_coords(grid, 'E')
grid[startx][starty] = 'a'
grid[endx][endy] = 'z'

todo.append((startx, starty, 0))


print("Part 1 : ", get_shortest_path())

todo = deque()

for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 'a':
                todo.append((i,j,0)) 

print("Part 2 : ", get_shortest_path())





