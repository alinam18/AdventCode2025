import os 
import re 
import sys 
import requests 
from bs4 import BeautifulSoup
from markdownify import markdownify

SESSION = '53616c7465645f5f9b25dba9527afd3a6ec2f63b1b239e758de04ff7bf49d3ab28dd82fc52cfd117f9eeb33e673f33293650ec613bc040640f0da8a502048c1f'

url = f"https://adventofcode.com/2025/"

try:

    response_url_input = requests.get(
        url,
        cookies={"session": SESSION},
    )
    response_url_input.raise_for_status()  
    day_input = response_url_input.text
except requests.exceptions.RequestException as e:
    print(f"Error fetching page cannot extract to md: {e}")
