import os 
import re
import sys
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify
# personal codes
import code


input_of_days = input("What day are you completing today? ")

while not input_of_days.isdigit():
    print("Please give me a valid number.")
    input_of_days = input("What day are you completing today? ")

path = f'day_{input_of_days}'
if not os.path.isdir(path):
    print(f"Directory day_{input_of_days} doesn't exist. Run start_new_day.py first.")
    sys.exit()



url = f"https://adventofcode.com/2025/day/{input_of_days}"


try:
    response = requests.get(url, cookies={"session": code.SESSION})
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, 'html.parser')
    day_description = soup.find_all(class_="day-desc")
    if len(day_description) < 2:
        print("Part 2 not unlocked yet.")
        sys.exit(1)
    part2_desc = day_description[1]
except requests.exceptions.RequestException as e:
    print(f"Error fetching page cannot extract to md: {e}")
    # exit()


with open(f"day_{input_of_days}/day_{input_of_days}_pt2.md", "w", encoding="utf-8") as file:
    md_text = markdownify(str(part2_desc), heading_style="ATX")
    file.write(md_text)



