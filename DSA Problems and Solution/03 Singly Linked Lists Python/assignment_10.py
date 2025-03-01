# In class SLL, define a method delete_first() to delete the first element from the list.

class SLL:
    def __init__(self, start=None):
        self.start = start

    def delete_first(self):
        if self.start != None:
            self.start = self.start.next
            