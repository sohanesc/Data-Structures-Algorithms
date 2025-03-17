# 4. Define a method insert_at_start() to insert an element at the start of the list.

def insert_at_start(self, data):
    new_node = Node(data) #type: ignore
    if self.is_empty():
        new_node.next = new_node
        self.last = new_node
    else:
        new_node.next = self.last.next
        self.last.next = new_node