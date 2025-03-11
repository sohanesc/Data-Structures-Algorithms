"""
Assignment-14: Deque Implementation using list
1. Define a class Deque to implement deque data structure using list. Define init method to create an empty list object as instance object member of Deque.
2. Define a method is_empty() to check if the deque is empty in Deque class.
3. In Deque class, define insert_front() method to add data at the front end of the deque.
4. In Deque class, define insert_rear() method to add data at the rear end of the deque.
5. In Deque class, define delete_front() method to remove front element from the deque.
6. In Deque class, define delete rear() method to remove rear element from the deque.
7. In Deque class, define get_front() method to return front element of the deque.
8. In Deque class, define get_rear() method to return rear element of the deque.
9. In Deque class, define size() method to return size of the deque that is number of items present in the deque.
"""

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def insert_front(self, data):
        self.items.insert(0, data)

    def insert_rear(self, data):
        self.items.append(data)
    
    def delete_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Deque is Empty")
        
    def delete_rear(self):
        if not self.is_empty():
            return self.items.pop(-1)
        else:
            raise IndexError("Deque is Empty")
            
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Deque is Empty")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Deque is Empty")
        
    def size(self):
        return len(self.items)
    

s1 = Deque()
s1.insert_front(10)
s1.insert_front(20)
s1.insert_rear(30)
s1.insert_rear(40)
s1.insert_rear(60)
print("Get Front Deque: ", s1.get_front())
print("Get Rear Deque: ", s1.get_rear())
print("Get Size of Deque: ", s1.size())
print("Remove Front Deque: ", s1.delete_front())
print("Remove Rear Deque: ", s1.delete_rear())
print("Get Size of Deque: ", s1.size())
print("Remove Front Deque: ", s1.delete_front())
print("Remove Rear Deque: ", s1.delete_rear())
print("Get Size of Deque: ", s1.size())