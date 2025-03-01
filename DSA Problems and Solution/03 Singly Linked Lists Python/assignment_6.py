# In class SLL, define a method search() to find the node with a specified element value.

class SLL:
    def __init__(self, start=None):
        self.start = start

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None