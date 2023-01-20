class RandomizedSet:

    def __init__(self):
        self.numHash = {}
        self.numList = []
        

    def insert(self, val: int) -> bool:
        if val not in self.numHash:
            self.numHash[val] = len(self.numList)
            self.numList.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val not in self.numHash:
            return False
        idx = self.numHash[val]
        temp = self.numList[-1]
        self.numList[idx] = self.numList[-1]
        self.numList.pop()
        self.numHash[temp] = idx
        del self.numHash[val]
        return True
        
        
    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()