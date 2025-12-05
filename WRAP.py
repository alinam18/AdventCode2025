import os 
import sys 
import requests 
from bs4 import BeautifulSoup
from markdownify import markdownify 
# personal codes
import code

intro_text = """
# Alina's Advent of Code Solution 2025 🎄
I am attempting to solve these puzzles!
Here is my current progress:

I'll try keep this as clea  as possible :)
"""

url = "https://adventofcode.com/2025/"

try:
    response = requests.get(
        url,
        cookies={"session": code.SESSION},
    )
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Check if the calendar actually exists on the page
    calendar_tag = soup.find(class_="calendar")
    
    if calendar_tag:
        # 2. Convert the HTML Tag object to a String, then to Markdown
        calendar_html = str(calendar_tag)
        calendar_md = markdownify(calendar_html)

        # 3. Write to file (Added .md extension for better previewing)
        with open("README.md", 'w', encoding="utf-8") as file:
            file.write(intro_text)
            file.write(calendar_md)
            
        print("Success! README.md created.")
    else:
        print("Could not find the calendar. Check your Session ID.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching page: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")