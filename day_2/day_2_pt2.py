import os
import re
import sys

def finding_factors(str_number):
    factors = []
    for i in range(1, len(str_number)):
        if len(str_number) % i == 0:
            factors.append(i)
    return factors

# if the pattern is invalid -> return False 
# if the pattern is VALID -> return True
def loop_check_for_valid(num, max_num_per_factor, str_number):
    pattern = []
    for each in range(num):
        pattern.append(str_number[each])
    # print(pattern)
    record = num
    for i in range(len(str_number)):
        pattern_char = pattern[i % num]
        target_char = str_number[i]

        if target_char == pattern_char:
            # Matches
            # print(f"matched at index {i} | Found {target_char} expected {pattern_char}")

            pass # (You can print here if you want debug info)
        else:
            # print(f"NO MATCH at index {i} | Found {target_char} expected {pattern_char}")
            return False
    # for each in range(record, max_num_per_factor):
    #     print(f"each {each} | str_number {str_number[each - 1]} ")
        # if str_number[] == pattern[each - 1]:
    return True

# if the pattern is invalid -> return False 
# if the pattern is VALID -> return True
def check_patterns(number):
    # if the number start with 0 its invalid 
    if str(number).startswith('0'):
        return False
    
    # return false if the number is invalid 
    # if odd number it cannot give an silly pattern 
    # print(number)
    # first find the first character 
    # find the next
    # if the len(number) = 3 -> only 1
    # 4 -> 1 or 2
    # 5 -> 1
    # 6 -> 1 or 2 or 3
    # 7 -> 1 
    # 8 -> 1 or 2 or 4
    # 9 -> 1 or 3 
    # 10 -> 1 or 2 or 5
    # first I need to find all the factors of each number 
    str_number = str(number)
    factors_list = finding_factors(str_number)

    for num in factors_list:
        # find how many of each num of factor list exists in number
        max_num_per_factor = int(len(str_number) / num)
        # print(f"per num {num} for {max_num_per_factor}")
        if loop_check_for_valid(num, max_num_per_factor, str_number):
            # print(f"Number Invalid here - {str_number}")
            return False
        # so for the max_num_per_factor time we need to repeat with the num in factor lists
        # for every num up until max_num_per_factor it mmyst check if its a vlid solution
    return True
    

    # print(f"{number} | {half}")


def finding_invalids(number):
    splited = number.split('-')
    startingRange = int(splited[0])
    endingRange = int(splited[1])

    count = startingRange
    number_of_invalids_lists = []
    while count <= endingRange:
        if not check_patterns(count):
            number_of_invalids_lists.append(count)
        count += 1
    return number_of_invalids_lists
    # count the number of invalid and the total for the invalids



def main ():
    # open_file = open('day_2_test.txt', 'r')
    open_file = open('day_2_input.txt', 'r')

    number_of_invalids_lists = []

    number_of_invalids_amounts = 0


    ranges = open_file.readline()
    ranges_list = ranges.split(',')
    total_invalid_id = 0
    # count = 0
    for all in ranges_list:
        invalids_lists = []
        invalids_lists.extend(finding_invalids(all))
        print(f"{all} has {len(invalids_lists)} invalids IDs, {invalids_lists}")
        for numbers in invalids_lists:
            total_invalid_id += numbers
    
    print(f"Adding up all the invalid IDs in this example produces {total_invalid_id}")


main()
