# In class SLL, implement iterator for SLL to access all the elements of the list in a sequence.

class SLL:
    def __init__(self, start=None):
        self.start = start 

    def __iter__(self):
        return SLLIterator(self.start)
class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration     # Exception Handling
        item = self.current.item
        self.current = self.current.next
        return item