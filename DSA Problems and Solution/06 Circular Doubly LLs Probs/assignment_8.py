# 8. In class CDLL, define a method to print all the elements of the list.

class CDLL:
    def print_list(self):
        temp = self.start
        if temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
            while temp is not self.start:
                print(temp.item, end=" ")
                temp = temp.next