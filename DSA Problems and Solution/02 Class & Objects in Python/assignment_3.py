# Define a class Rectangle with length and breadth as instance object variables. Provide setDimensions(), showDimensions(), and getArea() methods.


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def setDimensions(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def showDimensions(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)

    def getArea(self):
        area = self.length * self.breadth
        return area


r1 = Rectangle(10, 5)
r1.showDimensions()
area = r1.getArea()
print("Area:", area)
