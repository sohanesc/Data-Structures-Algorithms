# 11. Define a method delete_last() to delete the last element from the list.

def delete_last(self):
    if not self.is_empty():
        if self.last.next == self.last:
            self.last = None
        else:
            temp = self.last.next
            while temp.next != self.last:
                temp = temp.next
            temp.next = self.last.next
            self.last = temp