import os 
import re
import sys

input_of_days = input("What day are you completing today? ")

while not input_of_days.isdigit():
    print("Please give me a valid number.")
    input_of_days = input("What day are you completing today? ")

answer = input("Are you going to do both part? [y/n]")
while answer.lower() != 'y' and answer.lower() != 'n':
    answer = input("Are you going to do both part? [y/n]")


# make 
file_name = f"day_{input_of_days}"
os.makedirs(file_name, exist_ok=True)
print(f"Created new directry {file_name}.")

if answer.lower() != 'y':
    open(f"day_{input_of_days}/day_{input_of_days}.py", 'w')
    open(f"day_{input_of_days}/day_{input_of_days}.md", 'w')
else:
    open(f"day_{input_of_days}/day_{input_of_days}_pt1.py", 'w')
    open(f"day_{input_of_days}/day_{input_of_days}_pt1.py", 'w')
    open(f"day_{input_of_days}/day_{input_of_days}_pt2.py", 'w')
    open(f"day_{input_of_days}/day_{input_of_days}_pt2.py", 'w')

