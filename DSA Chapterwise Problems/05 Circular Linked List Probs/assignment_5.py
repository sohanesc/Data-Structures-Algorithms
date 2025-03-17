# 5. Define a method insert_at_last() to insert an element at the end of the list.

def insert_at_last(self, data):
    new_node = Node(data)   #type: ignore
    if self.is_empty():
        new_node.next = new_node
        self.last = new_node
    else:
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node