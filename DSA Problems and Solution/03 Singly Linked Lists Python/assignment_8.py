# In class SLL, define a method to print all the elements of the list.

class SLL:
    def __init__(self, start=None):
        self.start = start

    def print_list(self):
        temp = self.start
        while temp != None:
            print(temp.item, end=" ")
            temp = temp.next