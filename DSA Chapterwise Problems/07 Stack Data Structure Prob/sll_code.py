class Node:
    def __init__ (self, item=None, next=None):
        self.item = item
        self.next = next
        
class SLL:
    def __init__(self, start=None):
        self.start = start 

    # Define a method is_empty() to check if the linked list is empty in SLL class.
    def is_empty(self):
        return self.start is None
    
    # In class SLL, define a method insert_at_start() to insert an element at the start of the list.
    def insert_at_start(self, item):
        new_node = Node(item, self.start) 
        self.start = new_node   # or new_node.next = self.start

    # In class SLL, define a method insert_at_last() to insert an element at the end of the list.
    def insert_at_last(self, item):
        new_node = Node(item) 
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        else:
            self.start = new_node

    # In class SLL, define a method search() to find the node with a specified element value.
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    # In class SLL, define a method insert_after() to insert a new node after a given node of the list.
    def insert_after(self, temp, item):
        if temp is not None:
            new_node = Node(item, temp.next)
            temp.next = new_node

    # In class SLL, define a method to print all the elements of the list.
    def print_list(self):
        temp = self.start
        while temp != None:
            print(temp.item, end=" ")
            temp = temp.next

    # In class SLL, define a method delete_first() to delete the first element from the list.
    def delete_first(self):
        if self.start != None:
            self.start = self.start.next

    # In class SLL, define a method delete_last() to delete the last element from the list.
    def delete_last(self):
        if self.start != None:
            pass
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
    
    # In class SLL, define a method delete_item() to delete specified element from the list.
    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start       #first node reference 
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next


# In class SLL, implement iterator for SLL to access all the elements of the list in a sequence.
    def __iter__(self):
        return SLLIterator(self.start)
class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration     # Exception Handling
        item = self.current.item
        self.current = self.current.next
        return item
    


# # Driver Code
# mylist = SLL()
# mylist.insert_at_start(20)
# mylist.insert_at_start(10)
# mylist.insert_at_last(30)
# mylist.insert_after(mylist.search(20), 25)
# mylist.print_list()
# mylist.delete_item(30)
# print()
# # mylist.print_list()
# for x in mylist:
#     print(x, end=" ")

# print()