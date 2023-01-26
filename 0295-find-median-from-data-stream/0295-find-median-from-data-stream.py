class MedianFinder:

    def __init__(self):
        self.heap = []
        

    def addNum(self, num: int) -> None:
        bisect.insort(self.heap, num)
        # print(self.heap)


    def findMedian(self) -> float:
        l = len(self.heap)
        mid  = l // 2
        if l % 2 == 0:
            return (self.heap[mid] + self.heap[mid-1]) / 2
        return self.heap[mid]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()