import os 
import sys 

def main():
    # try:
    open_file = open("day_5_input.txt", "r")
    lines = open_file.readlines()


    valid_ranges = []
    
    check_mode = False
    count = 0
    check_range = []

    for line in lines:
        line = line.strip()
        
        
        
        parts = line.split('-')
        start = int(parts[0])
        end = int(parts[1])
        valid_ranges.append((start, end))
        for one, two in check_range:
            # skip will not put in check_range
            if one <= start <= two and one <= end <= two:
                continue
            # end is greater then two
            elif one <= start <= two and one <= end > two:
                # change the range of two into end
                check_range[one, end]
            elif one >= start <= two and one <= end <= two:
                check_range[start, two]
            
        if found:
            count += 1

    print(f"There are {count} available ingredients.")

main()