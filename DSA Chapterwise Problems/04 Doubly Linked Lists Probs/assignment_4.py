# 4. In class DLL, define a method insert_at_start() to insert an element at the starting of the list.

class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next
        
class DLL:
    def __init__(self, start = None):
        self.start = None

    def insert_at_start(self, item):
        new_node = Node(None, item, self.start)  #type: ignore
        if not self.is_empty():
            self.start.prev = new_node
        self.start = new_node