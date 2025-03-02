# 6. In class DLL, define a method search() to find the node with specified element value.

class DLL:
    def __init__(self, start = None):
        self.start = None

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

