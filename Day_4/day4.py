#AOC 2022 - Day 4

#Finding pair within another pair + overlaps

#Part 1 Answer : 540
#Part 2 Answer : 872

import os

file_path = os.path.join(os.path.dirname('__file__'), "day4.in")

with open(file_path) as file:

    count = 0
    range_count = 0
    
    for line in file:
        line = line.strip()

        split_numbers = []

        split_parts = line.split(",")
        split_numbers = [part.split("-") for part in split_parts]
        flattened_numbers = [int(item) for sublist in split_numbers for item in sublist]
    
        if len(flattened_numbers) == 4:
            split_numbers.append(flattened_numbers)

        for numbers in split_numbers:
            pass

        if (numbers[0] <= numbers[2]) and (numbers[1] >= numbers[3]):
                count += 1
                
        if (numbers[0] >= numbers[2]) and (numbers[1] <= numbers[3]):
                count += 1

        if (numbers[0] == numbers[2]) and (numbers[1] == numbers[3]):
                count -= 1
                
        overlap = False
        for i in range(numbers[0], numbers[1]+1):
            for j in range(numbers[2], numbers[3]+1):
                if i == j:
                    overlap  = True
                    
            if overlap == True:
                range_count += 1
                break

    print("Total Pairs : ", count)        
    print("Range Count : ", range_count)



file.close()