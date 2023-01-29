class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.data = [-1] * self.capacity
        self.size = 0
        

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.data.insert(0, value)
        self.size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.data[self.size] = value
        self.size += 1
        return True

    
    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.data.pop(0)
        self.size -= 1
        return True
    
    
    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.data.pop(self.size-1)
        self.size -= 1
        return True

    
    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.data[0]

    
    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.data[self.size - 1]

    
    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()