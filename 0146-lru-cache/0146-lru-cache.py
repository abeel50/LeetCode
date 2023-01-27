class Node:
    def __init__(self, k, v, next= None, prv= None):
        self.key, self.val = k, v
        self.next, self.prv = next, prv
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache= {}
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        self.lru.next, self.mru.prv = self.mru, self.lru
    
    # insert values at mru
    def insert(self, node):
        prv, next = self.mru.prv, self.mru
        prv.next, next.prv = node, node
        node.next, node.prv = next, prv
    
    # remove from doubly list
    def remove(self, node):
        next, prv = node.next, node.prv
        prv.next, next.prv = next, prv
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            toDel = self.lru.next
            print(toDel.key)
            self.remove(toDel)
            del self.cache[toDel.key]
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)