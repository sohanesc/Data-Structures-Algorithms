# 11. In class DLL, define a method delete_last() to delete last element from the list.

class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start = None):
        self.start = None

    def delete_last(self):
        if self.start == None:
            pass
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.prev.next = None