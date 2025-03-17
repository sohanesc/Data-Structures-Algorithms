# 8. Define a method to print all the elements of the list.

def print_list(self):
    if not self.is_empty():
        temp = self.last.next
        while temp != self.last:
            print(temp.item, end=" ")
            temp = temp.next
        print(temp.item)
