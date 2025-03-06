# 9. In class CDLL, implement iterator for CDLL to access all the elements of the list in a sequence.

class CDLL:
    def __iter__(self):
        return CDLLIterator(self.start)

class CDLLIterator:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.item
        self.current = self.current.next 
        return data