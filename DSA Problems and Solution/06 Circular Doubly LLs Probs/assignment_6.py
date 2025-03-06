# 6. In class CDLL, define a method search() to find the node with specified element value.

class CDLL:
    def search(self, data):
        temp = self.start
        if temp is None:
            return None
        if temp.item == data:
            return temp
        else:
            temp = temp.next
        while temp != self.start:
            if temp.item == data:
                return temp
            temp = temp.next
        return None