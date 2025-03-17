# In class SLL, define a method insert_at_start() to insert an element at the start of the list.

class SLL:
    def __init__(self, start=None):
        self.start = start

    def insert_at_start(self, item):
        new_node = Node(item, self.start) # type: ignore
        self.start = new_node   # or new_node.next = self.start
         