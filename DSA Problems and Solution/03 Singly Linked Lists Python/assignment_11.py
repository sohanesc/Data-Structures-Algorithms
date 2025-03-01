# In class SLL, define a method delete_last() to delete the last element from the list.

class SLL:
    def __init__(self, start=None):
        self.start = start

    def delete_last(self):
        if self.start != None:
            pass
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next != None:
                temp = temp.next
            temp.next = None