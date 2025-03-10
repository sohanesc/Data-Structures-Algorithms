"""
Assignment-12: Queue using list
1. Define a class Queue to implement queue data structure using list. Define init method to create an empty list object as instance object member of Queue.
2. Define a method is_empty() to check if the queue is empty in Queue class.
3. In Queue class, define enqueue() method to add data at the rear end of the queue.
4. In Queue class, define dequeue() method to remove front element from the queue.
5. In Queue class, define get_front() method to return front element of the queue.
6. In Queue class, define get_rear() method to return rear element of the queue.
7. In Queue class, define size() method to return size of the queue that is number of items present in the queue.
"""

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is Empty")
        
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is Empty")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is Empty")
        
    def size(self):
        return len(self.items)
    
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
