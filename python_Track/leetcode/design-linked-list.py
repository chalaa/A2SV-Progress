class Listnode:
    def __init__(self, val=0 , next=None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.val
    def addAtHead(self, val: int) -> None:
        temp = Listnode(val)
        temp.next = self.head
        self.head = temp
        self.size += 1
    
    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            temp =self.head
            new = Listnode(val)
            while temp.next:
                temp = temp.next
            temp.next = new
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index < self.size:
            new = Listnode(val)
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            new.next = temp.next
            temp.next = new
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            dummy = Listnode(0,self.head)
            temp = dummy
            for i in range(index):
                temp = temp.next
            if temp.next != None:
                temp.next = temp.next.next
            else:
                temp.next = None
            self.head = dummy.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)