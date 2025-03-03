# 10. Define a method delete_first() to delete the first element from the list.

def delete_first(self):
    if not self.is_empty():
        if self.last.next == self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next