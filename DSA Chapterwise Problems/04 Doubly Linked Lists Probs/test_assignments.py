class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start
    
    def is_empty(self):
        return self.start is None

    def insert_at_start(self, item):
        new_node = Node(None, item, self.start)
        if not self.is_empty():
            self.start.prev = new_node
        self.start = new_node

    def insert_at_last(self, data):
        if self.is_empty():
            self.start = Node(None, data, None)
        else:
            temp = self.start
            while temp.next:
                temp = temp.next
            new_node = Node(temp, data, None)
            temp.next = new_node

    def search(self, data):
        temp = self.start
        while temp:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp:
            new_node = Node(temp, data, temp.next)
            if temp.next:
                temp.next.prev = new_node
            temp.next = new_node

    def print_list(self):
        temp = self.start
        while temp:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def delete_first(self):
        if self.start:
            self.start = self.start.next
            if self.start:
                self.start.prev = None

    def delete_last(self):
        if self.start:
            if not self.start.next:
                self.start = None
            else:
                temp = self.start
                while temp.next:
                    temp = temp.next
                temp.prev.next = None

    def delete_item(self, data):
        temp = self.start
        while temp:
            if temp.item == data:
                if temp.next:
                    temp.next.prev = temp.prev
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.start = temp.next
                return
            temp = temp.next

    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


mylist = DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10), 15)

for x in mylist:
    print(x, end=" ")
print()
