#AOC - Day 2

#Rock Paper Scissors

#Part 1 Answer : 14827
#Part 2 Answer : 13889

import os

file_path = os.path.join(os.path.dirname('__file__'), "day2.in")

with open(file_path) as file:

    sum = 0

    part = int(input("Enter part (1 or 2) : "))

    for line in file:
        line = line.strip()

        if part == 1:

            if line:
                if line[2] == 'X':
                    sum += 1

                    if line[0] == 'A':
                        sum += 3

                    if line[0] == 'B':
                        sum += 0

                    if line[0] == 'C':
                        sum += 6
                    
                
                if line[2] == 'Y':
                    sum += 2

                    if line[0] == 'A':
                        sum += 6

                    if line[0] == 'B':
                        sum += 3

                    if line[0] == 'C':
                        sum += 0

                if line[2] == 'Z':
                    sum += 3

                    if line[0] == 'A':
                        sum += 0

                    if line[0] == 'B':
                        sum += 6

                    if line[0] == 'C':
                        sum += 3
        
        if part == 2:

            if line:
                if line[2] == 'X':
                    sum += 0

                    if line[0] == 'A':
                        sum += 3

                    if line[0] == 'B':
                        sum += 1

                    if line[0] == 'C':
                        sum += 2
                    
                
                if line[2] == 'Y':
                    sum += 3

                    if line[0] == 'A':
                        sum += 1

                    if line[0] == 'B':
                        sum += 2

                    if line[0] == 'C':
                        sum += 3

                if line[2] == 'Z':
                    sum += 6

                    if line[0] == 'A':
                        sum += 2

                    if line[0] == 'B':
                        sum += 3

                    if line[0] == 'C':
                        sum += 1



print("Total Score : ", sum)