# Cybersecurity professionals use web scraping to crawl the web and extract information from target websites.
# python BeautifulSoub library is used to scrap contents from website. Write a python program to get the h1 content
# and display the title of website. 
# Input format:
#  Input the url of the website.
# Output format:
# Prints the title content of a page.
# display "Website not found" if the provided url is invalid.
# print "No h1 tag is present in website" if there is no h1 tag is in the provided website.
# Sample Input and Output 1:
# Enter website URL:
# https://www.example.com
# Example Domain
# Sample Input and Output 2:
# Enter website URL:
# https://www.google.com/
# No h1 tag is present in website

import requests
from bs4 import BeautifulSoup

def get_title(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('h1')
            if title:
                return title.text.strip()
            else:
                return "No h1 tag is present in website"
        else:
            return "Website not found"
    except requests.exceptions.RequestException as e:
        return "Website not found"

def main():
    url = input("Enter website URL:\n")
    title = get_title(url)
    print(title)

if __name__ == "__main__":
    main()

