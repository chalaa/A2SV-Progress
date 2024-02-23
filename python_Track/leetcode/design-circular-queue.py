class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.size = k
        self.left = 0
        self.right = 0

    def enQueue(self, value: int) -> bool:
        if self.right - self.left == self.size:
            return False
        self.queue.append(value)
        self.right += 1
        return True
        
    def deQueue(self) -> bool:
        if self.right == self.left:
            return False
        self.left += 1
        return True
    
    def Front(self) -> int:
        if self.left == self.right:
            return -1
        return self.queue[self.left]
    def Rear(self) -> int:
        if self.left == self.right:
            return -1
        return self.queue[self.right-1]

    def isEmpty(self) -> bool:
        return self.left == self.right

    def isFull(self) -> bool:
        return self.right - self.left == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()