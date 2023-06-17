#AOC 2022 - Day 5

#Moving stacks

#Part 1 Answer : JRVNHHCSJ
#Part 2 Answer : GNFBSBJLH

import os

file_path = os.path.join(os.path.dirname('__file__'), "day5.in")

list1 = ['V', 'R', 'H', 'B', 'G', 'D', 'W']
list2 = ['F', 'R', 'C', 'G', 'N', 'J']
list3 = ['J', 'N', 'D', 'H', 'F', 'S', 'L']
list4 = ['V', 'S', 'D', 'J']
list5 = ['V', 'N', 'W', 'Q', 'R', 'D', 'H', 'S']
list6 = ['M', 'C', 'H', 'G', 'P']
list7 = ['C', 'H', 'Z', 'L', 'G', 'B', 'J', 'F']
list8 = ['R', 'J', 'S']
list9 = ['M', 'V', 'N', 'B', 'R', 'S', 'G', 'L']

with open(file_path) as file:

    part = int(input("Enter part (1 or 2) : "))

    for line in file:
        line = line.strip()

        numbers = []
        current_num = ''

        for char in line:

            if char.isdigit():
                current_num += char
            
            elif current_num != "":
                numbers.append(int(current_num))
                current_num = ""

        if current_num != "":
            numbers.append(int(current_num))

        
        if part == 1:
        

            for i in range(numbers[0]):

                from_list = "list" + str(numbers[1])
                sample_list = globals()[from_list]
                element = sample_list.pop(0)

                to_list = "list" + str(numbers[2])
                sample_list = globals()[to_list]
                sample_list.insert(0, element)

        if part == 2:

            if numbers[0] > 1 :
 
                new_list = []

                for i in range(numbers[0]):
                    from_list = "list" + str(numbers[1])
                    sample_list = globals()[from_list]
                    element = sample_list.pop(0)

                    new_list.append(element)

                to_list = "list" + str(numbers[2])
                sample_list = globals()[to_list]
                sample_list[:0] = new_list

            else:

                from_list = "list" + str(numbers[1])
                sample_list = globals()[from_list]
                element = sample_list.pop(0)

                to_list = "list" + str(numbers[2])
                sample_list = globals()[to_list]
                sample_list.insert(0, element)


letter_message = list1[0] + list2[0] + list3[0] + list4[0] + list5[0] + list6[0] + list7[0] + list8[0] + list9[0]


print("Message : ", letter_message)