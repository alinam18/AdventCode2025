import os
import sys
import re

def find_the_largest_joltage(each_line):
    str_line = str(each_line)
    if len(str_line) < 2:
        return int(str_line)
    first_digit = str_line[0]
    second_digit = str_line[1]
    str_digit = first_digit + second_digit
    digit = int(str_digit)
    for i in range(len(str_line)):
        for j in range(i + 1, len(str_line)):
            #    combine the two string
            current_str_digit = str_line[i] + str_line[j]
            current_digit = int(current_str_digit)
            if current_digit > digit:
                digit = current_digit
        
    return digit

def main():
    open_file = open('day_3_input.txt', 'r')  
    # open_file = open('day3_test.txt', 'r')  

    lines = open_file.readlines()
    # print(lines)
    cleaned_line = []
    for each_line in lines:
        cleaned = each_line.strip()
        cleaned_line.append(cleaned)

    print(cleaned_line)
    total_joltage = 0
    for each_line in cleaned_line:
        joltage = find_the_largest_joltage(each_line)
        print(f"Largest Joltage {joltage}")
        total_joltage += joltage

    print(f"The total Joltage is {total_joltage}")



main()