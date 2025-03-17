# 3. Define a method is_empty() to check if the linked list is empty in DLL class.

class DLL:
    def __init__(self, start = None):
        self.start = start 
    
    def is_empty(self):
        return self.start is None