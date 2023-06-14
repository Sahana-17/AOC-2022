#AOC - Day 3

#Finding priority values from list of strings

#Part 1 Answer : 7817
#Part 2 Answer : 2444

import os

file_path = os.path.join(os.path.dirname('__file__'), "day3.in")

with open(file_path) as file: 

    priority = 0
    part = int(input("Enter part (1 or 2) : "))

    alpha_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 
                'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 
                'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 
                'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 
                'B' : 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 
                'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41,
                'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48,
                'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

    if part == 1:

        for line in file:
            line = line.strip()


            first_compartment = ''
            second_compartment = ''
            share_item = ''

            length = len(line)

            for i in range(length):

                if i < (length/2):
                    first_compartment += line[i]
                else:
                    second_compartment += line[i]

                for j in range(len(first_compartment)):
                    for z in range(len(second_compartment)):

                        if first_compartment[j] == second_compartment[z]:

                            if first_compartment[j] != share_item:
                                share_item = first_compartment[j]
                                
            priority += alpha_dict[share_item]

        
        print("Priority : ", priority)

    if part == 2:
        
        lines = file.readlines()

        for i in range(0, len(lines), 3):
             
            line1 = lines[i].strip()
            line2 = lines[i+1].strip()
            line3 = lines[i+2].strip()
        
            share_item = set(line1) & set(line2) & set(line3)

            char_set = share_item
            character = list(char_set)[0]

            priority += alpha_dict[character]   

        print("Priority : ", priority)  

file.close()