class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.data = [-1] * self.capacity
        self.insert = 0
        self.out = 0
        self.size = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.data[self.insert] = value
        self.insert = (self.insert + 1) % self.capacity
        self.size += 1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.data[self.out] = -1
        self.out = (self.out + 1) % self.capacity
        self.size -= 1
        return True


    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.data[self.out]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.data[(self.insert - 1) % self.capacity]


    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.capacity == self.size

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()