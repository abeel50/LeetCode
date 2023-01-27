class CustomStack:

    def __init__(self, maxSize: int):
        self.st = []
        self.size = maxSize
        
    def isEmpty(self):
        return len(self.st) == 0
    
    def isFull(self):
        return len(self.st) == self.size
    
    def push(self, x: int) -> None:
        if not self.isFull():
            self.st.append(x)
        

    def pop(self) -> int:
        if self.isEmpty(): return -1
        ele = self.st[-1]
        self.st.pop()
        return ele
    

    def increment(self, k: int, val: int) -> None:
        if k <= len(self.st):
            end = k
        else: 
            end = len(self.st)
        for i in range(end):
            self.st[i] += val
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)