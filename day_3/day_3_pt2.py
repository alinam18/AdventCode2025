import os
import sys
import re

def checking_last_digit(current_i, digit_left, str_line):
    # conver the digit into array 
    j =  current_i 
    for i in range(j, len(str_line) - digit_left + 1):
        # print(f"str_line[i] = {str_line[i]} |str_line[current_i] = {str_line[current_i]} | i = {i} | current_i = {current_i} ")
        if str_line[i] > str_line[current_i]:
            current_i = i
    return_array = [current_i, str_line[current_i]]
        
    return return_array


def find_the_largest_joltage(each_line):
    str_line = str(each_line)
    if len(str_line) < 12:
        return int(str_line)
    digit = int(str_line[:12])
    # print(digit)

    # the amount of buffer numbers I can have 
    buffer_amount = len(str_line) - 12
    largest_list = []
    digit_left = 12
    current_i = 0
    while len(largest_list) < 12:
        return_array = checking_last_digit(current_i, digit_left, str_line)
        largest_list.append(return_array[1])
        # print(f"largest_list
        #  so far - {largest_list} | current_i={current_i} | return_array0={return_array[0]} | return_array1={return_array[1]} | digit_left={digit_left}")
        number = return_array[1]
        current_i = return_array[0] + 1
        digit_left -= 1

    

    # separator = ", "
    string_digits = [str(d) for d in largest_list]
    largest_joltage = int("".join(string_digits))
    return largest_joltage

def main():
    open_file = open('day_3_input.txt', 'r')  
    # open_file = open('day3_test.txt', 'r')  

    lines = open_file.readlines()
    # print(lines)
    cleaned_line = []
    for each_line in lines:
        cleaned = each_line.strip()
        cleaned_line.append(cleaned)

    # print(cleaned_line)
    total_joltage = 0
    count = 0
    for each_line in cleaned_line:
        joltage = (find_the_largest_joltage(each_line))
        # joltage is list rn 
        print(f"Largest Joltage {joltage}")
        total_joltage += joltage
        # count += 1
        # if count > 1:
        #     # print(len(each_line))
        #     break

    # The total Joltage is 166345822896410
    print(f"The total Joltage is {total_joltage}")



main()