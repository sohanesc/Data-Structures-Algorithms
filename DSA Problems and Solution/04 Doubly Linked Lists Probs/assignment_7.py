# 7. In class DLL, define a method insert_after() to insert a new node after a given node of the list.

class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start = None):
        self.start = None

    def insert_after(self, temp, data):
        if temp is not None:
            new_node = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = new_node
            temp.next = new_node
            