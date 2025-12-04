import pandas as pd 
import os 
import re

open_file = open('day_1_pt_input.txt', 'r')
# open_file = open('day1_test.txt', 'r')
rotations_lists = open_file.readlines()

# set initial location to 50
location = 50
newValue = 50
count = 0
for rotation in rotations_lists:
    # split the input 
    if 'L' in rotation:
        direction = re.split(r'L', rotation)
        value = int(direction[1])
        newValue = newValue - value
    elif 'R' in rotation:
        direction = re.split(r'R', rotation)
        value = int(direction[1])
        newValue = newValue + value

    while newValue > 99 or newValue < 0:
        if newValue > 99:
            # for 99 
            newValue = newValue - 100
        elif newValue < 0:
            # less than 0
            newValue = newValue + 100


    cleaned_rotation = rotation.strip()

    print(f"The dial is rotated {cleaned_rotation} to point at {newValue}.")
    if newValue == 0:
        count += 1



print(f"The dial points at 0 a total of {count} times.")