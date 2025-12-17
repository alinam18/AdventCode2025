from typing import TypedDict, List

# Your Blueprint
class ColumnData(TypedDict):
    index: int
    numbers: List[int]

def multiplications(number_list):
    print(number_list)
    number = 1
    for x in number_list:
        number = number * int(x)
    return number



def addition(number_list):
    print(number_list)
    number = 0
    for x in number_list:
        number += int(x)
    return number

def calculate(columns):
    print(columns)
    # multiplications
    number = 0
    if columns['numbers'][-1] == '*':
        print("multiplications")
        del columns['numbers'][-1]
        number = multiplications(columns['numbers'])

    elif columns['numbers'][-1] == '+':
        print("addition")
        del columns['numbers'][-1]
        number = addition(columns['numbers'])
    return number


def main():
    # lines = open("test.txt", "r").readlines()
    lines = open("day_6_input.txt", "r").readlines()
    
    temp_columns = {}

    for line in lines:
        line = line.strip()
        
        
        # Split the line into individual numbers
        row_numbers = [(x) for x in line.split()]
        print(f"line{line} row_numbers {row_numbers}")

        # Loop through this row's numbers
        for i, num in enumerate(row_numbers):
            # If this column bucket doesn't exist yet, create it
            if i not in temp_columns:
                temp_columns[i] = []
            
            # Add the number to the correct column bucket
            temp_columns[i].append(num)

    final_results: List[ColumnData] = []
    
    for col_index, values in temp_columns.items():
        new_item: ColumnData = {
            "index": col_index,
            "numbers": values
        }
        final_results.append(new_item)

    # print(final_results)
    total_number = 0
    for columns in final_results:
        total_number += calculate(columns)
    print(f"Total number {total_number}")

main()