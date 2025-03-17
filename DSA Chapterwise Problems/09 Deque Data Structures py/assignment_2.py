"""
Assignment-15: Deque using Doubly Linked List Concept
1. Define a class Node with instance object member variables prev, item and next.
2. Define a class Deque to implement deque data structure using doubly linked list concept. Define init () method to initialise front and rear reference variable; and item_count variable to keep track of number of elements in the deque.
3. Define a method is_empty() to check if the deque is empty in Deque class.
4. In Deque class, define insert_front() method to add data at the front of the deque.
5. In Deque class, define insert_rear() method to add data at the rear of the deque.
6. In Deque class, define delete_front() method to remove front element from the deque.
7. In Deque class, define delete_rear() method to remove rear element from the deque.
8. In Deque class, define get_front() method to return front element of the deque.
9. In Deque class, define get_rear() method to return rear element of the deque.
10. In Deque class, define size() method to return size of the deque that is number of items present in the deque.
"""

class Node:
    def __init__(self, item = None, prev = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0
    
    def insert_front(self, data):
        new_node = Node(data, None, self.front)
        if not self.is_empty():
            self.front.prev = new_node
            self.front = new_node
        else:
            self.front = self.rear = new_node
        self.item_count += 1
        return self.front 
    
    def insert_rear(self, data):
        new_node = Node(data, self.rear, None)
        if not self.is_empty():
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node
        self.item_count += 1
        return self.rear
    
    def delete_front(self):
        if not self.is_empty():
            self.front = self.front.next
            self.front.prev = None
        # elif self.front == self.rear:
        #     self.front = self.rear = None
        else:
            raise IndexError("Deque is Empty")
        self.item_count -= 1
        return self.front.item
        
    def delete_rear(self):
        if not self.is_empty():
            self.rear.next = None
            self.rear = self.rear.prev
        # elif self.front == self.rear:
        #     self.front = self.rear = None
        else:
            raise IndexError("Deque is Empty")
        self.item_count -= 1
        return self.rear.item
        
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Deque is Empty")
        
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Deque is Empty")
        
    def size(self):
        return self.item_count
    
s1 = Deque()
s1.insert_front(10)
s1.insert_front(20)
s1.insert_front(30)
s1.insert_front(40)
s1.insert_rear(50)
print("Get Size: ", s1.size())
print("Get Front: ", s1.get_front())
print("Get Rear: ", s1.get_rear())
print("Remove Front: ", s1.delete_front())
print("Remove Rear: ", s1.delete_rear())
print("Get Size: ", s1.size())