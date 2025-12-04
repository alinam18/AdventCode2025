# import pandas as pd 
# import os 
# import re

# open_file = open('day_1_pt1_input.txt', 'r')
# # open_file = open('day_test.txt', 'r')
# rotations_lists = open_file.readlines()

# # set initial location to 50
# location = 50
# newValue = 50
# count = 0
# for rotation in rotations_lists:
#     # split the input 
#     if 'L' in rotation:
#         direction = re.split(r'L', rotation)
#         value = int(direction[1])
#         newValue = newValue - value

#     elif 'R' in rotation:
#         direction = re.split(r'R', rotation)
#         value = int(direction[1])
#         newValue = newValue + value

#     # this is the new position
#     new_position = (newValue) % 100
#     zero_pass_counter = abs(newValue // 100)
#     count += zero_pass_counter

#     while newValue > 99 or newValue < 0:
#         if newValue > 99:
#             # for 99 
#             newValue = newValue - 100
#             # new_position = (location + newValue) % 100
#         elif newValue < 0:
#             # less than 0
#             newValue = newValue + 100
#             # new_position = (location + newValue) % 100


#     cleaned_rotation = rotation.strip()

#     print(f"The dial is rotated {cleaned_rotation} to point at {newValue}. | {new_position} | {zero_pass_counter}")
#     # if newValue == 0:
#     #     count += 1



# print(f"The dial points at 0 a total of {count} times.")

import re

with open('day_1_pt1_input.txt', 'r') as f:
    rotations_lists = [line.strip() for line in f if line.strip()]

position = 50      
zero_hits = 0       

for rotation in rotations_lists:
    direction = rotation[0]
    value = int(rotation[1:])

    if direction == 'L':
        step = -1
    elif direction == 'R':
        step = 1

    for number in range(value):
        position = (position + step) % 100
        if position == 0:
            zero_hits += 1

print(f"The dial points at 0 a total of {zero_hits} times.")
