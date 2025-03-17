# In class SLL, define a method insert_at_last() to insert an element at the end of the list.

class SLL:
    def __init__(self, start=None):
        self.start = start

    def insert_at_last(self, item):
        new_node = Node(item) # type: ignore
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        else:
            self.start = new_node