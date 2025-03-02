# 5. In class DLL, define a method insert_at_last() to insert an element at the end of the list.

class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start = None):
        self.start = None

    def insert_at_last(self, item):
        temp = self.start                # temp points to the start of the list
        if self.start != None:           # check if the list is not empty
            while temp.next != None:     # find the last node where temp.next is None
                temp = temp.next         # temp iterates to the last node
            
        new_node = Node(temp, data, None) # type: ignore
        if temp != None:
            temp.next = new_node
        else:
            self.start = new_node



