#AOC 2022 - Day 1 

#Finding total calories 

import os

file_path = os.path.join(os.path.dirname('__file__'), "day1.in")

with open(file_path) as file:

    max_value = 0
    total_sum = 0
    max_list = []

    for line in file:
        line = line.strip()  
        
        if line:
            total_sum += int(line)

        else:
            max_list.append(total_sum) 
            total_sum = 0

    max_list.append(total_sum)
    max_list.sort(reverse = True)      

    max_value = sum(max_list[:3]) #Modified for part 1 and 2

print("Maximum calories :", max_value)
