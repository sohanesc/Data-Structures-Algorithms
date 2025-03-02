# 10. In class DLL, define a method delete_first() to delete first element from the list.

class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start = None):
        self.start = None

    def delete_first(self):
        if self.start != None:
            self.start = self.start.next
            if self.start != None:
                self.start.prev = None
                