#AOC 2022 - Day 6

#Distinct characrters

#Part 1 Answer : 1760
#Part 2 Answer : 2974

import os

file_path = os.path.join(os.path.dirname('__file__'), "day6.in")

with open(file_path) as file:

    entire_file = file.read()

marker = 0
distinct = 0

part = int(input("Enter part (1 or 2) : "))

if part == 1:
    distinct = 4
elif part == 2:
    distinct = 14

length = (len(entire_file)) - (distinct+1)

for i in range(length):
    if len(set(entire_file[i:i+(distinct)])) == distinct:
        marker = marker + (i+distinct)
        break
print("First Marker : ", marker)