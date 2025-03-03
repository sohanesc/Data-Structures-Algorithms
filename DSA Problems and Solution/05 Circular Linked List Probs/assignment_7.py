# 7. Define a method insert_after() to insert a new node after a given node in the list.

def insert_after(self, temp, data):
    if temp != None:
        new_node = Node(data, temp.next) #type: ignore
        temp.next = new_node
        if temp == self.last:
            self.last = new_node