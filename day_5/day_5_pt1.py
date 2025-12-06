import os 
import sys 

def main():
    # try:
    open_file = open("day_5_input.txt", "r")
    lines = open_file.readlines()


    valid_ranges = []
    
    check_mode = False
    count = 0

    for line in lines:
        line = line.strip()
        
        # Handle switching modes
        if not line:
            check_mode = True
            continue
            
        if not check_mode:
            # PARSING: Just store the start and end numbers!
            parts = line.split('-')
            start = int(parts[0])
            end = int(parts[1])
            valid_ranges.append((start, end))
            
        else:
            target = int(line)
            found = False
            
            # Look through our rules
            for start, end in valid_ranges:
                if start <= target <= end:
                    found = True
                    break 
                
            if found:
                count += 1

    print(f"There are {count} available ingredients.")

main()