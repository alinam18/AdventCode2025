import os 
import sys 
import requests 
from bs4 import BeautifulSoup
from markdownify import markdownify # Make sure to install this: pip install markdownify

# 1. Use an environment variable or a placeholder for safety
# SESSION = os.getenv("AOC_SESSION") 
SESSION = '53616c7465645f5f9b25dba9527afd3a6ec2f63b1b239e758de04ff7bf49d3ab28dd82fc52cfd117f9eeb33e673f33293650ec613bc040640f0da8a502048c1f'

url = "https://adventofcode.com/2025/"

try:
    response = requests.get(
        url,
        cookies={"session": SESSION},
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
            file.write(calendar_md)
            
        print("Success! README.md created.")
    else:
        print("Could not find the calendar. Check your Session ID.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching page: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")