# In class SLL, define a method insert_after() to insert a new node after a given node of the list.

class SLL:
    def __init__(self, start=None):
        self.start = start

    def inser_after(self, node, item):
        if node is not None:
            new_node = node(item, node.next)
            node.next = new_node
        