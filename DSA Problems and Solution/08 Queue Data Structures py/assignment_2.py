"""
Assignment-13: Queue using Singly Linked List Concept
1. Define a class Queue to implement queue data structure using singly linked list concept. Define init () method to initialise front and rear reference variable; and item_count variable to keep track of number of elements in the queue.
2. Define a method is_empty() to check if the queue is empty in Queue class.
3. In Queue class, define enqueue() method to add data into the queue.
4. In Queue class, define dequeue() method to remove front element from the queue.
5. In Queue class, define get_front() method to return front element of the queue.
6. In Queue class, define get_rear() method to return rear element of the queue.
7. In Queue class, define size() method to return size of the queue that is number of items present in the queue.
"""

class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0
        
    def enqueue(self, data):
        new_node = Node(data)
        if not self.is_empty():
            self.rear.next = new_node
        else:
            self.front = new_node
        self.rear = new_node
        self.item_count += 1
            
    def dequeue(self):
        if not self.is_empty():
            removed_item = self.front.item
            self.front.item = None
            self.front = self.front.next
        else:
            raise IndexError("Queue is Empty")
        self.item_count -= 1
        return removed_item

    
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Queue is Empty")
        
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Queue is Empty")
        
    def size(self):
        return self.item_count
    
s1 = Queue()
s1.enqueue(10)
s1.enqueue(20)
s1.enqueue(30)
print("Size of Queue: ", s1.size())
print("Front of Queue: ", s1.get_front())
print("Rear of Queue: ", s1.get_rear())
print("Removed element: ", s1.dequeue())
print("Size of Queue: ", s1.size())
print("Front of Queue: ", s1.get_front())
print("Rear of Queue: ", s1.get_rear())