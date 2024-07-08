# Write a python program to get the a paragraph contents in the website and display it.
# Python BeautifulSoub library is used to scrap contents from website.
# Input format:
# Html code is given as a part of template code. 
# Output format:
# Prints the paragraph content from html.
# Sample Input and Output 1:
# This domain is for use in illustrative examples in documents.
# You may use this domain in literature without prior coordination or asking for permission.
# More information...

from bs4 import BeautifulSoup

def extract_paragraphs(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all <p> tags
    paragraphs = soup.find_all('p')
    
    # Print each paragraph content
    for paragraph in paragraphs:
        print(paragraph.text.strip())

# Sample Input as HTML content
html_content = """
<html>
<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
"""

# Call the function with the provided HTML content
extract_paragraphs(html_content)
