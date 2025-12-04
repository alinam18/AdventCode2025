import os
import re
import sys

# if the pattern is invalid -> return False 
# if the pattern is VALID -> return True
def check_patterns(number):
    # if the number start with 0 its invalid 
    if str(number).startswith('0'):
        return False
    
    # return false if the number is invalid 
    # if odd number it cannot give an silly pattern 
    if len(str(number)) % 2 != 0:
        # always valid
        return True
    
    half = int(len(str(number)) / 2)
    str_number = str(number)
    first_half = 0
    last_half = half

    for i in range(half):
        # print(f"{str_number} | {str_number[first_half]} and {str_number[last_half]} | at {first_half} and {last_half}")
        if str_number[first_half] != str_number[last_half]:
            return True
        first_half += 1
        last_half += 1
    return False
    

    # print(f"{number} | {half}")


def finding_invalids(number):
    splited = number.split('-')
    startingRange = int(splited[0])
    endingRange = int(splited[1])

    # length = len(endingRange - startingRange)
    # print(f"starting range = {startingRange}, ending range = {endingRange}")
    # for numbers in range(endingRange - startingRange):
    #     pri?nt(numbers)
    count = startingRange
    number_of_invalids_lists = []
    while count <= endingRange:
        if not check_patterns(count):
            # print(f"This number is invalid {count}")
            number_of_invalids_lists.append(count)
        # logics
        # print(count)
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
        # count += 1
        # if count == 3:
        #     break
        # print(all)
        for numbers in invalids_lists:
            total_invalid_id += numbers
    
    print(f"Adding up all the invalid IDs in this example produces {total_invalid_id}")


main()
