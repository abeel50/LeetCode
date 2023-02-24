class MinStack:

    def __init__(self):
        self.st = [] #for stack
        self.minHash = {} # for min tracking
        
    def getlen(self):
        return len(self.st)
        
    def push(self, val: int) -> None:
        # if stack and hash is empty
        if len(self.st) == 0:
            self.minHash[(val, self.getlen())] = val
            self.st.append(val)
        else:
            t = self.st[-1]
            curMin =  self.minHash[(t, self.getlen()-1)]
            #if new val is less than previous min
            if val < curMin:
                self.minHash[(val, self.getlen())] = val
            else: #otherwise previous min is intact
                self.minHash[(val, self.getlen())] = curMin
            self.st.append(val)
        # print("Push: ", val , self.minHash, self.st)


    def pop(self) -> None:
        if len(self.st) == 0: return
        t = self.st[-1]
        del self.minHash[(t, self.getlen()-1)]
        self.st.pop()

    def top(self) -> int:
        if len(self.st) == 0: return None
        return self.st[-1]

    def getMin(self) -> int:
        return self.minHash[(self.top(), self.getlen()-1)]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()