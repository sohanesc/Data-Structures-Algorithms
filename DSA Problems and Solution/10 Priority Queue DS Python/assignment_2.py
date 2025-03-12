"""
Assignment-17: Priority queue using linked list
1. Define a Node class with instance member variables item, priority and next.
2. Define a class PriorityQueue to implement priority queue data structure using singly linked list. Provide init () method to create a start reference variable (initially containing None) and item_count variable (initially 0).
3. Define a push method in PriorityQueue class to insert new data with given priority.
4. Define a pop method in PriorityQueue class, which returns the highest priority data stored in the priority queue data structure. Raise exception if priority queue is empty.
5. Define is_empty method in PriorityQueue class to check if the priority queue is empty.
6. In class PriorityQueue, define a method size to return the number of elements present in the priority queue.
"""

class Node:
    def __init__(self, item = None, priority = None, next = None):
        self.item = item
        self.priority = priority
        self.next = next

class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def push(self, data, priority):
        new_node = Node(data, priority)
        if self.is_empty() or priority < self.start.priority:
            new_node.next = self.start
            self.start = new_node
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.item_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("PQ is Empty")
        data = self.start.item
        self.start = self.start.next
        self.item_count -= 1
        return data
    
    def size(self):
        return self.item_count
    
s1 = PriorityQueue()
s1.push(42, 2)
s1.push('Python', 6)
s1.push(99.99, 8)
s1.push(3.14, 10)
s1.push([1, 2, 3], 1)
s1.push({'key': 'value'}, 3)
print("The Size of PQ: ", s1.size())

while not s1.is_empty():
    print(s1.pop())

print("The Size of PQ: ", s1.size())
