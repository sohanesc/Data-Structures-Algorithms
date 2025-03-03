# 12. Define a method delete_item() to delete a specified element from the list.

def delete_item(self,data):
        if not self.is_empty():
            if self.last.next==self.last:
                if self.last.item==data:
                    self.last=None
            else:
                if self.last.next.item==data:
                    self.delete_first()
                else:
                    temp=self.last.next

                    while temp!=self.last:
                        if temp.next==self.last:
                            if self.last.item==data:
                                self.delete_last()
                            break
                        if temp.next.item==data:
                            temp.next=temp.next.next
                            break
                        temp=temp.next
            