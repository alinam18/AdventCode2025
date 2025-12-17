import os 
import sys 

def main():
    # try:
    open_file = open("day_5_input.txt", "r")
    # open_file = open("day_5_test.txt", "r")
    lines = open_file.readlines()


    valid_ranges = []
    
    check_mode = False
    count = 0
    check_range = []
    ranges = []
    end = False
    # list them and sort them 
    for line in lines:
        # clean
        if line == '\n':
            end = True
            break
        line = line.strip()
        digit =  line.split("-")
        # print(digit)
        # line.digit[0]
        ranges.append([int(digit[0]), int(digit[1])])

    ranges.sort(key=lambda x: int(x[0]))
    print(ranges)
    # next now we will compare the second digit only 
    new_range = []
    for index, numbers in enumerate(ranges):
        print(f"checking {numbers} | {new_range}")
        comparing_value_1 = numbers[0]
        comparing_value_2 = numbers[1]
        # print(comparing_value)
        if not new_range:
            new_range.append(numbers)
            continue
        else:
            add = False
            for n_index, n_numbers in enumerate(new_range):
                # if curr_one <= two and one <= curr_two:
                if n_numbers[0] <= comparing_value_2 and comparing_value_1 <= n_numbers[1]: 
                    add = True
                    print(f"overlapping n_numbers:{n_numbers} | comparing_value_1:{comparing_value_1} | comparing_value_2:{comparing_value_2}")
                    new_start = min(n_numbers[0], comparing_value_1)
                    new_end = max(n_numbers[1], comparing_value_2)
                    new_range[n_index] = [new_start, new_end]
                    # print(f"{new_range[n_index]}")
            


            if add == False:
                new_range.append(numbers)

    # now calculate
    amount = 0
    for numbers in new_range:
        end = numbers[1]
        start = numbers[0]
        amount += (end - start) + 1
        # print(amount)

    # print()
    print(f"Final {amount}: {new_range}")
    # Final 344813017450467
    print(f"Final {amount}")





main()