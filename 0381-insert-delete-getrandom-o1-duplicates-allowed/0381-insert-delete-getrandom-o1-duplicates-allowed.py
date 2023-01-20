class RandomizedCollection:

    def __init__(self):
        # {1:(0,3), 2:(1,2), 3(4)}
        self.numHash = defaultdict(set)
        self.numList = []
        

    def insert(self, val: int) -> bool:
        #add val to hash map set
        self.numHash[val].add(len(self.numList))
        #append in list
        self.numList.append(val)
        return len(self.numHash[val]) == 1
        

    def remove(self, val: int) -> bool:
        if not self.numHash[val]: return False
        #remove is index of val to remove
        remove, last = self.numHash[val].pop(), self.numList[-1]
        self.numList[remove] = last
        self.numHash[last].add(remove)
        self.numHash[last].discard(len(self.numList) - 1)
        self.numList.pop()
        return True  
        
        

    def getRandom(self) -> int:
        return random.choice(self.numList)

        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()