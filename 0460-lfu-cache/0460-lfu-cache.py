class Node:
    def __init__(self, val, count):
        self.value = val
        self.count = count
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys ={}
        self.counts = defaultdict(OrderedDict)
        self.minCount= None
    
    # sets Min Count    
    def setMinCount(self, c):
        if len(self.counts[c]) == 0:
            del self.counts[c]
        if len(self.counts.keys()) > 0:
            self.minCount= min(self.counts.keys())
        else:
            self.minCount = None
        
        
    def get(self, key: int) -> int:
        # print("Getting Key: ", key)
        if key not in self.keys: return -1
        
        node = self.keys[key]
        node.count += 1
        
        del self.counts[node.count - 1][key]
        self.counts[node.count][key] = True
        
        self.keys[key] = node
        self.setMinCount(node.count-1)
        # print( self.keys,"\n", self.counts)
        return node.value


    def put(self, key: int, value: int) -> None:
        if not self.capacity: return
        
        # print("Putting Key: ", key)
        
        # if key is alreday in the system
        if key in self.keys:
            node = self.keys[key]
            node.value = value
            node.count += 1
            del self.counts[node.count - 1][key]
            self.counts[node.count][key] = True
            self.keys[key] = node
            self.setMinCount(node.count-1)
            # print( self.keys,"\n",self.counts)
            return 
        
        if len(self.keys) == self.capacity:
            lfuKey, temp = self.counts[self.minCount].popitem(last=False)
            self.setMinCount(self.minCount)
            del self.keys[lfuKey]
            
        node = Node (value, 1)
        self.minCount = 1
        self.keys[key] = node
        self.counts[self.minCount][key] = True
        # print( self.keys,"\n", self.counts)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)