"""
Assignment-8: Stack extending list
1. Define a class Stack to implement stack data structure by extending list class.
2. Define a method is_empty() to check if the stack is empty in Stack class.
3. In Stack class, define push() method to add data onto the stack.
4. In Stack class, define pop() method to remove top element from the stack.
5. In Stack class, define peek() method to return top element on the stack.
6. In Stack class, define size() method to return size of the stack that is number of items present in the stack.
7. Implement a way to restrict use of insert() method of list class from stack object.
"""

class Stack(list):
    def is_empty(self):
        return len(self) == 0
    
    def push(self, data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty")
        
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
        
    def size(self):
        return len(self)

    def insert(self, index, data):
        raise AttributeError("No attribute 'insert' in Stack.")

s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Peek value: ", s1.peek())
print("Peek value: ", s1.pop())
print("Peek value: ", s1.peek())