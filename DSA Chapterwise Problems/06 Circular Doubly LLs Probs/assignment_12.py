# 12. In class CDLL, define a method delete_item() to delete specified element from the list.

class CDLL:
    def delete_item(self, data):
        if self.start is not None:
                temp = self.start
                if temp.item == data:
                    self.delete_first()
                else:
                    temp = temp.next
                    while temp is not self.start:
                        if temp.item == data:
                            temp.next.prev = temp.prev
                            temp.prev.next = temp.next
                            