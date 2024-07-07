# Write a python program to get the item name, link and price of the book and display it.
# Method	Description
# def find_item_name()	This method read the HTML and prints the name of a item.
# def rating()    	This method read the HTML and prints the rating of a item.
# Input format:
#  HTML code is given in a template code.
# Output format:
# Prints the item rating. 
# Sample Input and Output 1:
# A Light in the Attic
# Three

from bs4 import BeautifulSoup

html = """
<html>
        <body>
            <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
                <article class="product_pod">
                        <div class="image_container">
                                <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
                        </div>
                            <p class="star-rating Three">
                                <i class="icon-star"></i>
                                <i class="icon-star"></i>
                                <i class="icon-star"></i>
                                <i class="icon-star"></i>
                                <i class="icon-star"></i>
                            </p>
                        <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the Attic</a></h3>
                        <div class="product_price">
                    <p class="price_color">£51.77</p>
            <p class="instock availability">
                <i class="icon-ok"></i>
                    In stock
            </p>
        </p>
        <form>
            <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
        </form>
    </article>
    </li>
    </body>
</html>
"""

simple_soup = BeautifulSoup(html, 'html.parser')

def find_item_name():
    item_name = simple_soup.find('h3').find('a').get('title')
    print(item_name)

def rating():
    rating_class = simple_soup.find('p', class_='star-rating').get('class')
    rating = rating_class[1] if len(rating_class) > 1 else "No Rating"
    print(rating)

find_item_name()
rating()

