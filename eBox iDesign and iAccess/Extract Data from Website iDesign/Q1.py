# Write a python program to get the links used in the website and display the links.
# Python BeautifulSoub library is used to scrap contents from website.
# Input format:
# Html code is given as a part of template code. 
# Output format:
# Prints the links in a html content.
# Sample Input and Output 1:
# https://www.iana.org/domains/example

html = """
<html>
<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
    