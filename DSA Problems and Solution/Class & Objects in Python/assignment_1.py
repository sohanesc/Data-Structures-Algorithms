# Define a python class Person with instance object variables name and age. Set instance object variables in the __init__() method. Also define the show() method to display the name and age of a person.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}\nAge: {self.age}")


person1 = Person("Sohan Sahoo", 69)
person1.show()
