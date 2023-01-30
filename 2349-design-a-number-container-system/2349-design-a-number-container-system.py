from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.container = {}
        self.indexHash = defaultdict(SortedList)
        

    def change(self, index: int, number: int) -> None:
        if index in self.container:
            prv = self.container[index]
            self.indexHash[prv].discard(index)
            if len(self.indexHash[prv]) == 0:
                del self.indexHash[prv] 
        self.container[index] = number
        self.indexHash[number].add(index)
    
    def find(self, number: int) -> int:
        return self.indexHash[number][0] if number in self.indexHash else -1            
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)