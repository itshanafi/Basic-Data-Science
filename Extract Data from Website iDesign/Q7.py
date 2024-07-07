# Write a python program to get the item name, link and price of the book and display it.
# Method	Description
# def find_item_name()        	This method reads the item name and displays the item name.
# def find_item_link()	This method displays the item link.
# def find_item_price	This methos displays the item price.
# Input format:
#  HTML code is given in a template code.
# Output format:
# Prints the item name, link and price. 
# Sample Input and Output 1:
# A Light in the Attic
# catalogue/a-light-in-the-attic_1000/index.html
# £51.77

from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
            <article class="product_pod">
                <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html">
                        <img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail">
                    </a>
                </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
                <h3>
                    <a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the Attic</a>
                </h3>
                <div class="product_price">
                    <p class="price_color">£51.77</p>
                    <p class="instock availability">
                        <i class="icon-ok"></i>
                        In stock
                    </p>
                </div>
                <form>
                    <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
                </form>
            </article>
        </li>
    </body>
</html>
"""

def find_item_name():
    soup = BeautifulSoup(html, 'html.parser')
    item_name = soup.find('h3').a.text.strip()
    print(item_name)

def find_item_link():
    soup = BeautifulSoup(html, 'html.parser')
    item_link = soup.find('h3').a['href']
    print(item_link)

def find_item_price():
    soup = BeautifulSoup(html, 'html.parser')
    item_price = soup.find('p', class_='price_color').text.strip()[1:]  # Remove the currency symbol (£)
    print(item_price)

# Call the functions to display the item details
find_item_name()
find_item_link()
find_item_price()
