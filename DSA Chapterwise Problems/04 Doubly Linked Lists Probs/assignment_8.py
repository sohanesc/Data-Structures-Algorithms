# 8. In class DLL, define a method to print all the elements of the list.

class DLL:
    def __init__(self, start = None):
        self.start = None

    def print_list(self):
        temp = self.start
        while temp != None:
            print(temp.item, end=" ")
            temp = temp.next