class OrderedStream:

    def __init__(self, n: int):
        self.size = n
        self.data = dict.fromkeys(range(1, self.size + 1), None)
        self.ptr = 1
        
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey] = value
        res  = []
        for i in range(self.ptr, self.size + 1):
            if not self.data[i]:
                break
            else:
                res.append(self.data[i])
                self.ptr += 1
        if idKey == self.ptr:
            self.ptr += 1
        return res
                

        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)