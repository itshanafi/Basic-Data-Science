# Write a python program to perform web scraping and extract information from an HTML document
# and displays the tags in html content. Python BeautifulSoub library is used to scrap contents from website.
# Input format:
# Html file is given as a part of template code. 
# Output format:
# Prints the tags inside the tag class.
# Sample Input and Output 1:
# love
# inspirational
# life
# humor
# books
# reading
# friendship
# friends
# truth
# simile

from bs4 import BeautifulSoup

def extract_tags(html_content, tag_class):
    soup = BeautifulSoup(html_content, 'html.parser')
    tags = soup.find_all(class_=tag_class)
    for tag in tags:
        print(tag.text.strip())

# Assuming sample.html contains your HTML content
with open('sample.html', 'r') as file:
    html_content = file.read()

extract_tags(html_content, 'your-class-name')  # Replace 'your-class-name' with the actual class name
