import os 
import sys 
import re 
def check(checking_row, checking_col, cleaned_pattern):
    # for col_index, line in enumerate(cleaned_pattern):
    #     for row_index, symbols in enumerate(line):
    #         if checking_col == col_index and checking_row == row_index and symbols == '@':
    #             # print(f"True : checking_row {checking_row}, checking_col {checking_col}, {symbols}")
    #             return True
    if cleaned_pattern[checking_row][checking_col] == '@':
        return True
    return False
            
    # return False
def check_surroundings(col_index, row_index, cleaned_pattern, symbols):
    found = 0
    grid_search = [
        (-1,-1), (-1, 0), (-1, 1),
        (0, -1),  (0, 1), 
        (1, -1), (1, 0), (1, 1)
    ]


    for search_y, search_x in grid_search:
        checking_row = row_index + search_x
        checking_col = col_index + search_y
        # print(f"checking_row {checking_row}, checking_col {checking_col}, len(cleaned_pattern) {len(cleaned_pattern)}")

        if 0 <= checking_row < len(cleaned_pattern) and 0 <= checking_col < len(cleaned_pattern[0]):
            if check(checking_row, checking_col, cleaned_pattern):
                # print(f"True : row_index {row_index} | {checking_row}, col_index {col_index} | {checking_col}, {symbols}")

                found += 1
    # print(f"found = {found}")
    return found

def grid_search(cleaned_pattern):
    count = 0
    rolls = 0
    for row_index, line in enumerate(cleaned_pattern):
        print(f"row_index: {row_index}, Value: {line}")
        for col_index, symbols in enumerate(line):
            # print(symbols)

            # print(symbols)
            count = 0
            if symbols == '@':
                # check the surrounding
                found = int(check_surroundings(col_index, row_index, cleaned_pattern, symbols))
                count += found
                print(f"col_index = {col_index}, row_index= {row_index}, found = {found}, symbols {symbols}")
                if found < 4:
                    rolls += 1
                    # print(f"True : row_index {row_index}, col_index {col_index}, {symbols}")

                # print(f"col_index {col_index}, row_index: {row_index}, symbols: {symbols}")
            # break
        # if row_index == 9:
        # break
        
    return rolls

def cleanning(pattern):
    cleaned_pattern = []
    for i in pattern:
        cleaned_pattern.append(i.strip())
    # print(cleaned_pattern)
    return cleaned_pattern

def main():
    # open_file = open('day_4_test.txt', "r")
    open_file = open('day_4_input.txt', "r")
    pattern = open_file.readlines()
    cleaned_pattern = cleanning(pattern)
    count = grid_search(cleaned_pattern)
# There are 1411 rols of paper
    print(f"There are {count} rols of paper")

main()