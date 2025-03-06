# 4. In class CDLL, define a method insert_at_start() to insert an element at the starting of the list.

class CDLL:
    def insert_at_start(self, data):
        new_node = Node(item = data)   #type: ignore
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.start
            new_node.prev = self.start.prev
            self.start.prev.next = new_node
            self.start.prev = new_node
        self.start = new_node