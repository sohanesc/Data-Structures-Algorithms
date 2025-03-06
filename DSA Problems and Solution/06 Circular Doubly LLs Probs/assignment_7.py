# 7. In class CDLL, define a method insert_after() to insert a new node after a given node of the list.

class CDLL:
    def insert_after(self, temp, data):
        if temp is not None:
            new_node = Node(item = data)   #type: ignore
            new_node.next = temp.next 
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node