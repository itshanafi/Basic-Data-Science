# Implement a Python script that lets users input a URL to scrape.
# The script should fetch and parse the HTML content using requests and BeautifulSoup.
# Extract all links and email addresses from the page. Ensure cybersecurity by using a legitimate user-agent string,
# implementing timeouts, and handling exceptions. Remind users to adhere to ethical scraping practices.
# Requirements:
# Implement a function fetch_and_parse(url) that takes a URL as input and uses the requests library to fetch the content.
# Handle potential exceptions and return a BeautifulSoup object for parsed HTML.
# Implement a function extract_info(soup) that takes a parsed HTML BeautifulSoup object as input.
# Extract all links from the page and find email addresses using regular expressions. Return a dictionary containing the extracted data.
# In the main function:
# Prompt the user to input a target URL.
# Call the fetch_and parse function with the user-provided URL.
# If parsing is successful, call the extract_info function and display the extracted data.
# Incorporate cybersecurity considerations such as:
# Mimic a legitimate browser's user-agent string in headers.
# Implement timeouts for requests to prevent long delays.
# Properly handle exceptions to ensure the script remains robust.
# Remind the user to respect ethical guidelines and website terms of service.
# Sample input & output1:
# Enter the URL to scrape: https://pro.e-box.co.in
# Extracted data: {'links': [], 'emails': []}

import requests
from bs4 import BeautifulSoup
import re

def fetch_and_parse(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching and parsing the URL: {e}")
        return None
    
def extract():
    links = []
    emails = []
    soup = fetch_and_parse(url)
    if soup:
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        for email in re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.get_text()):
            emails.append(email)
    return {'links': links, 'emails': emails}

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    extracted_data = extract()
    print("Extracted data:", extracted_data)
