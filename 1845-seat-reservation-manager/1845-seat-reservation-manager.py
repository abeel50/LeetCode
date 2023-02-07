class SeatManager:

    def __init__(self, n: int):
        self.reserved = defaultdict(bool)
        self.available = []
        self.SIZE, self.booked= n, 0
        self.batch = 100
        self.start, self.end = 1, self.batch
        self.setHeap()
        
    # sets heap according to constraints
    def setHeap(self):
        # if heap size is less than Batch size
        # then heap Size is MAx number of seats
        if self.SIZE < self.batch:
            self.available = [*range(1, self.SIZE + 1)]
        else:
            #initilize heap batch
            self.available = [*range(self.start, self.end + 1)]
            self.start = self.end + 1
            self.end += self.batch
        heapq.heapify(self.available)
        
    # if all seats are booked 
    def isFull(self):
        return self.booked == self.SIZE
    
    # adds heap batch
    def addHeapBatch(self):
        # if no more seats
        if self.isFull(): return
        # if any space is available in previous batch
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