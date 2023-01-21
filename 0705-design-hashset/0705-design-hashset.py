class MyHashSet:

    def __init__(self):
        self.hash = defaultdict(int)
        

    def add(self, key: int) -> None:
        self.hash[key] = 1
        

    def remove(self, key: int) -> None:
        if self.contains(key):
            del self.hash[key]

    def contains(self, key: int) -> bool:
        return key in self.hash
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)