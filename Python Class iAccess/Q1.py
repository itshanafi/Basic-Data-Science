# Create a base Class Shape and derive the CalAreaSquare, CalAreaRectangle, CalAreaTriangle, CalAreaCircle classes.
# Use the following method in base class Shape:
# Method Name            Description
# area()                 Display the input parmaters
# Calculate area of square in all the derived classes:
# Method Name            Description
# area()                 Find the area of the Square, Rectangle, Triganle and Circle, in their respective derived classes.
# Note: The area of triangle=0.5*base*height
# pi value will be considered as 3.14

class Shape:
    def area(self):
        pass

class CalAreaSquare(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Side of Square :", self.side)
        return self.side ** 2

class CalAreaRectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Length of Rectangle :", self.length)
        print("Breadth of Rectangle :", self.width)
        return self.length * self.width

class CalAreaTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print("Base of Triangle :", self.base)
        print("Height of Triangle :", self.height)
        return 0.5 * self.base * self.height

class CalAreaCircle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Radius of Circle :", self.radius)
        return 3.14 * (self.radius ** 2)

def main():
    print("Select an Option")
    print("1.Square")
    print("2.Rectangle")
    print("3.Triangle")
    print("4.Circle")

    option = int(input())
    
    if option == 1:
        side = int(input("Enter the side\n"))
        square = CalAreaSquare(side)
        print("Area of Square :", square.area())

    elif option == 2:
        length = int(input("Enter the length\n"))
        width = int(input("Enter the breadth\n"))
        rectangle = CalAreaRectangle(length, width)
        print("Area of Rectangle :", rectangle.area())

    elif option == 3:
        base = int(input("Enter the base\n"))
        height = int(input("Enter the height\n"))
        triangle = CalAreaTriangle(base, height)
        print("Area of Triangle : {:.2f}".format(triangle.area()))

    elif option == 4:
        radius = int(input("Enter the radius\n"))
        circle = CalAreaCircle(radius)
        print("Area of Circle : {:.2f}".format(circle.area()))

    else:
        print("Invalid option")

if __name__ == "__main__":
    main()


#############################################################################################


class Shape:
    def __init__(self):
        pass
    
    def display_parameters(self):
        pass

class CalAreaSquare(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    
    def display_parameters(self):
        print(f"Side of Square: {self.side}")
    
    def area(self):
        return self.side ** 2

class CalAreaRectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def display_parameters(self):
        print(f"Length of Rectangle : {self.length}")
        print(f"Breadth of Rectangle : {self.width}")
    
    def area(self):
        return self.length * self.width

class CalAreaTriangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
    
    def display_parameters(self):
        print(f"Base of Triangle : {self.base}")
        print(f"Height of Triangle : {self.height}")
    
    def area(self):
        return 0.5 * self.base * self.height

class CalAreaCircle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def display_parameters(self):
        print(f"Radius of Circle : {self.radius}")
    
    def area(self):
        return 3.14 * (self.radius ** 2)

def main():
    print("Select an Option")
    print("1.Square")
    print("2.Rectangle")
    print("3.Triangle")
    print("4.Circle")
    
    option = int(input())
    
    if option == 1:
        side = int(input("Enter the length\n"))
        square = CalAreaSquare(side)
        square.display_parameters()
        print(f"Area of Square : {square.area()}")
    elif option == 2:
        length = int(input("Enter the length\n"))
        width = int(input("Enter the breadth\n"))
        rectangle = CalAreaRectangle(length, width)
        rectangle.display_parameters()
        print(f"Area of Rectangle : {rectangle.area()}")
    elif option == 3:
        base = int(input("Enter the base\n"))
        height = int(input("Enter the height\n"))
        triangle = CalAreaTriangle(base, height)
        triangle.display_parameters()
        print(f"Area of Triangle : {triangle.area():.2f}")
    elif option == 4:
        radius = int(input("Enter the radius\n"))
        circle = CalAreaCircle(radius)
        circle.display_parameters()
        print(f"Area of Circle : {circle.area():.2f}")
    else:
        print("Invalid option. Please enter a valid choice (1/2/3/4).")

if __name__ == "__main__":
    main()

