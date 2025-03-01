# Define a class Book with instance object variables bookid, title, and price. Initialize them via the __init__() method. Also define a method to show book variables.


class Book:
    def __init__(self, bookid, title, price):
        self.bookid = bookid
        self.title = title
        self.price = price

    def show(self):
        print("Book ID:", self.bookid)
        print("Title:", self.title)
        print("Price:", self.price)


book1 = Book(1, "Almanack of Naval Ravikant", 0.00)
book1.show()
