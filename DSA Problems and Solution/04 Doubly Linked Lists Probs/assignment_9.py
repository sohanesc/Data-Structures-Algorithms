# 9. In class DLL, implement iterator for DLL to access all the elements of the list in a sequence.

class DLL:
    def __init__(self, start = None):
        self.start = start 

    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data