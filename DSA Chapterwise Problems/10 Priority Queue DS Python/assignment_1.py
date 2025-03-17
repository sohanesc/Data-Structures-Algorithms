"""
Assignment-16: Priority queue using list
l. Define a class PriorityQueue to implement priority queue data structure using list. Provide __init__() method to create a list object (initially empty).
2. Define a push method in PriorityQueue class to insert new data with given priority.
3. Define a pop method in PriorityQueue class, which returns the highest priority data stored in the priority queue data structure. Raise exception if priority queue is empty
4. Define is_empty method in PriorityQueue class to check if the priority queue is empty.
5. In class PriorityQueue, define a method size to return the number of elements present in the priority queue.
"""

class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data, priority):
        index = 0
        while index < len(self.items) and self.items[index][1] <= priority:
            index += 1
        self.items.insert(index,(data, priority))

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)[0]
        else:
            raise IndexError("PriorityQueue is Empty")
        
    def size(self):
        return len(self.items)
    

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