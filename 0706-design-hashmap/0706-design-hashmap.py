class MyHashMap:

    def __init__(self):
        self.hash = []
        

    def put(self, key: int, value: int) -> None:
        for i, (k,v) in enumerate(self.hash):
            if k == key:
                self.hash[i] = (key,value)
                return    
        self.hash.append((key,value))

    def get(self, key: int) -> int:
        for k,v in self.hash:
            if k == key:
                return v  
        return -1
        

    def remove(self, key: int) -> None:
        idx = -1
        for i, (k,v) in enumerate(self.hash):
            if k == key:
                idx = i
        if idx >= 0:
            del self.hash[idx]
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)