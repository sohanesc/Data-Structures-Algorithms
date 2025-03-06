# 5. In class CDLL, define a method insert_at_last() to insert an element at the end of the list.

class CDLL:
    def insert_at_last(self, data):
        new_node = Node(item = data)   #type: ignore
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.start = new_node
        else:
            new_node.next = self.start
            new_node.prev = self.start.prev
            new_node.prev.next = new_node
            self.start.prev = new_node
