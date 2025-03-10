"""
Assignment-11: Stack Implementation by extending Singly Linked List
1. Import module containing singly linked list code in your python file.
2. Define a class Stack to implement stack data structure by inheriting SLL class.
3. Define a method is_empty() to check if the stack is empty in Stack class.
4. In Stack class, define push() method to add data onto the stack.
5. In Stack class, define pop() method to remove top element from the stack.
6. In Stack class, define peek() method to return top element on the stack.
7. In Stack class, define size() method to return size of the stack that is number of items present in the stack.
"""

from sll_code import *

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0

    def is_empty(self):
        return super().is_empty()
    
    def push(self, data):
        self.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count -= 1
            return self.start.item
        else:
            raise IndexError("Stack is Empty")
    
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is Empty")
        
    def size(self):
        return self.item_count
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("The Size of Stack: ", s1.size())
print("The Peek of Stack: ", s1.peek())
print("The Poped of Stack: ", s1.pop())
print("The Peek of Stack: ", s1.peek())
print("The Size of Stack: ", s1.size())
print("The Poped of Stack: ", s1.pop())
print("The Peek of Stack: ", s1.peek())
print("The Size of Stack: ", s1.size())