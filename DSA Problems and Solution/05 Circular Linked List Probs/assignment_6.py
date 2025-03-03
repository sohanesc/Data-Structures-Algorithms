# 6. Define a method search() to find the node with a specified element value.

def search(self, data):
    if self.is_empty():
        return None
    temp = self.last.next
    while temp != self.last:
        if temp.item == data:
            return temp
        temp = temp.next
    if temp.item == data:
        return temp
    return None