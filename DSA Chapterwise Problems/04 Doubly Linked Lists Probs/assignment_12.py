# 12. In class DLL, define a method delete_item() to delete specified element from the list.

class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start = None):
        self.start = None

    def delete_item(self, data):
        if self.start == None:          # if list is empty
            pass
        else:                           # if list has more than one node
            temp = self.start
            while temp != None:         # traverse the list
                if temp.item == data:   # if data is found
                    if temp.next != None:
                        temp.next.prev = temp.prev
                    if temp.prev != None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next