# Write a python program to perform web scraping and extract information from an HTML document and displays the contents.
# Python BeautifulSoub library is used to scrap contents from website. Write a program to display the content inside the given tag.
# Input format:
# The first line of input contains the website URL.
# The second line of input contains the tag name.
# Output format:
# Prints the contents inside the tag.
# display "Website not found" if the provided url is invalid.
# print "No h1 tag is present in website" if there is no h1 tag is in the provided website.
# Sample Input and Output:
# Enter website URL:
# https://www.example.com
# Enter tag:
# p
# This domain is for use in illustrative examples in documents. You may use this
#     domain in literature without prior coordination or asking for permission.

from bs4 import BeautifulSoup
import requests

def main():
    url = input("Enter website URL:\n")
    tag = input("Enter tag:\n")
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if soup.find(tag):
            print(soup.find(tag).text.strip())
        else:
            print(f"No {tag} tag is present in website")
    else:
        print("Website not found. Status code:", response.status_code)

if __name__ == "__main__":
    main()


