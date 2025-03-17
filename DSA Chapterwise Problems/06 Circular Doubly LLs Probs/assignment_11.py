# 11. In class CDLL, define a method delete_last() to delete last element from the list.

class CDLL:
    def delete_last(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev