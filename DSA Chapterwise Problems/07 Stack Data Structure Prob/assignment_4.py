"""
Assignment-10: Stack using Linked List
1. Import module containing singly linked list code in your python file.
2. Define a class Stack to implement stack data structure. Define __init__() method to create Singly Linked List (SLL) object.
3. Define a method is_empty() to check if the stack is empty in Stack class.
4. In Stack class, define push() method to add data onto the stack.
5. In Stack class, define pop() method to remove top element from the stack.
6. In Stack class, define peek() method to return top element on the stack.
7. In Stack class, define size() method to return size of the stack that is number of items present in the stack.
"""

from sll_code import *

class Stack:
    def __init__(self):
        self.sll = SLL()
        self.item_count = 0

    def is_empty(self):
        return self.sll.is_empty()
    
    def push(self, data):
        self.sll.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            self.sll.delete_first()
            self.item_count -= 1
            return self.sll.start.item
        else:
            raise IndexError("Stack is Empty")
        
    def peek(self):
        if not self.is_empty():
            return self.sll.start.item
        else:
            raise IndexError("Stack is Empty")
        
    def size(self):
        return self.item_count
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Total Elements: ", s1.size())
print("Peek Element: ", s1.peek())
print("Poped Element: ", s1.pop())
print("Total Elements: ", s1.size())
print("Peek Element: ", s1.peek())
print("Poped Element: ", s1.pop())
print("Total Elements: ", s1.size())
