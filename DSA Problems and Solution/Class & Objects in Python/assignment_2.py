# Define a class Circle with an instance object variable radius. Provide setter and getter for radius. Also define getArea() and getCircumference() methods.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def setradius(self, radius):
        self.radius = radius

    def getradius(self):
        return self.radius

    def getArea(self):
        area = 3.14 * self.radius * self.radius
        return area

    def getCircumference(self):
        circumference = 2 * 3.14 * self.radius
        return circumference


circle1 = Circle(5)
print("Radius:", circle1.getradius())
print("Area:", circle1.getArea())
print("Circumference:", circle1.getCircumference())
