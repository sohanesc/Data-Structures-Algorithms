class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

class CDLL:
    def __init__(self, start = None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        new_node = Node(item = data)
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.start
            new_node.prev = self.start.prev
            self.start.prev.next = new_node
            self.start.prev = new_node
        self.start = new_node

    def insert_at_last(self, data):
        new_node = Node(item = data)
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.start = new_node
        else:
            new_node.next = self.start
            new_node.prev = self.start.prev
            new_node.prev.next = new_node
            self.start.prev = new_node

    def search(self, data):
        temp = self.start
        if temp is None:
            return None
        if temp.item == data:
            return temp
        else:
            temp = temp.next
        while temp != self.start:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            new_node = Node(item = data)
            new_node.next = temp.next 
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node

    def print_list(self):
        temp = self.start
        if temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
            while temp is not self.start:
                print(temp.item, end=" ")
                temp = temp.next

    def delete_first(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next

    def delete_last(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev

    def delete_item(self, data):
        if self.start is not None:
                temp = self.start
                if temp.item == data:
                    self.delete_first()
                else:
                    temp = temp.next
                    while temp is not self.start:
                        if temp.item == data:
                            temp.next.prev = temp.prev
                            temp.prev.next = temp.next


    def __iter__(self):
        return CDLLIterator(self.start)

class CDLLIterator:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.item
        self.current = self.current.next 
        return data
    
mylist = CDLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(30), 35)

for x in mylist:
    print(x, end=" ")

print()
