# Write a python program to get the book details that a book price ranges between the given minimum and maximum price.
# Python BeautifulSoub library is used to scrap contents from website.
# Use https://books.toscrape.com/ website to scrap book details.
# The book details are contained within <article> elements with the class product_pod.
# Input format:
# The first line of input is minimum price.
# The second line of input is maximum price.
# Output format:
# Prints the book name and price.
# Sample Input and Output 1:
# Enter the minimum amount
# 5
# Enter the maximum amount
# 15
# Books between £5.00 and £15.00:
# Title: Starving Hearts (Triangular Trade Trilogy, #1)
# Price: £13.99

import requests
from bs4 import BeautifulSoup

base_url = 'http://books.toscrape.com/'

# Input minimum and maximum price
minimum_price = float(input("Enter the minimum amount\n"))
maximum_price = float(input("Enter the maximum amount\n"))

# Make request to the website and parse with BeautifulSoup
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all book articles with class 'product_pod'
books = soup.find_all('article', class_='product_pod')

print(f"Books between £{minimum_price:.2f} and £{maximum_price:.2f}:")

for book in books:
    # Extract title and price of the book
    book_title = book.h3.a['title']
    book_price = float(book.find('p', class_='price_color').text.strip('£'))

    # Check if the book price is within the specified range
    if minimum_price <= book_price <= maximum_price:
        print("Title:", book_title)
        print("Price: £{:.2f}".format(book_price))
        print()
