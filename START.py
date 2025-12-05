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


answer = input("Are you going to do both part? [y/n]")
while answer.lower() != 'y' and answer.lower() != 'n':
    answer = input("Are you going to do both part? [y/n]")

# extract the url
url = f"https://adventofcode.com/2025/day/{input_of_days}#part2"
url_input = f"https://adventofcode.com/2025/day/{input_of_days}/input"

# try url
try:
    response = requests.get(url)
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, 'html.parser')
    day_description = soup.find(class_="day-desc")
except requests.exceptions.RequestException as e:
    print(f"Error fetching page cannot extract to md: {e}")
    # exit()

# try url_input
try:

    response_url_input = requests.get(
        url_input,
        cookies={"session": code.SESSION},
    )
    # response_url_input = requests.get(url_input)
    response_url_input.raise_for_status()  
    day_input = response_url_input.text

except requests.exceptions.RequestException as e:
    print(f"Error fetching page cannot extract to md: {e}")
    # exit()

# find the description
# make 
    
file_name = f"day_{input_of_days}"
os.makedirs(file_name, exist_ok=True)
print(f"Created new directry {file_name}.")

if answer.lower() != 'y':
    open(f"day_{input_of_days}/day_{input_of_days}.py", 'w')

    mdfile = f"day_{input_of_days}/day_{input_of_days}.md"

    if day_description:
        md_text = markdownify(str(day_description), heading_style="ATX")
        with open(mdfile, "w", encoding="utf-8") as file:
            file.write(md_text)
    else:
        open(f"day_{input_of_days}/day_{input_of_days}.md", 'w')

    pt1_input_file = f"day_{input_of_days}/day_{input_of_days}_input.txt"
    if day_input:
        with open(pt1_input_file, "w", encoding="utf-8") as file:
            file.write(day_input)

else:
    open(f"day_{input_of_days}/day_{input_of_days}_pt1.py", 'w')
    mdfile = f"day_{input_of_days}/day_{input_of_days}_pt1.md"
    if day_description:
        md_text = markdownify(str(day_description), heading_style="ATX")
        with open(mdfile, "w", encoding="utf-8") as file:
            file.write(md_text)
    else:
        open(mdfile, 'w')

    # place in the input of the files in a txt as well 
    
    pt1_input_file = f"day_{input_of_days}/day_{input_of_days}_input.txt"

    if day_input:
        with open(pt1_input_file, "w", encoding="utf-8") as file:
            file.write(day_input)

    open(f"day_{input_of_days}/day_{input_of_days}_pt2.py", 'w')
    open(f"day_{input_of_days}/day_{input_of_days}_pt2.md", 'w')

