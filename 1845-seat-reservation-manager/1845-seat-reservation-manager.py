class SeatManager:

    def __init__(self, n: int):
        self.SIZE, self.booked= n, 0
        self.reserved = defaultdict(bool)
        self.batch = 10
        self.start , self.end = 1 , self.batch
        self.available = []
        self.setHeap()
        
    def setHeap(self):
        if self.SIZE < self.batch:
            self.available = [*range(1, self.SIZE + 1)]
        else:
            self.available = [*range(self.start, self.end + 1)]
            self.start = self.end + 1
            self.end += self.batch
        heapq.heapify(self.available)
    
    def isFull(self):
        return self.booked == self.SIZE
    
    def addHeapBatch(self):
        if self.isFull(): return
        if len(self.available) > 0: return
        self.available = [*range (self.start, self.end + 1)]
        self.start = self.end + 1
        self.end += self.batch
        heapq.heapify(self.available)        

    def reserve(self) -> int:
        seat = heapq.heappop(self.available)
        self.reserved[seat] = True
        self.booked += 1
        self.addHeapBatch()
        return seat

    def unreserve(self, seatNumber: int) -> None:
        del self.reserved[seatNumber]
        self.booked -= 1
        heapq.heappush(self.available, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)