import requests
from bs4 import BeautifulSoup
import re

# Define the code/pattern to match
code_to_match = r'specific-code-pattern'

# Function to fetch and scan a webpage
def scan_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Search for the code pattern
        if re.search(code_to_match, soup.prettify()):
            print(f"Match found at: {url}")
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

# Example URLs to check
urls = [
    "https://example.com",
    "https://another-example.com",
    # Add more URLs
]

for url in urls:
    scan_page(url)
