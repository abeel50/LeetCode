from sortedcontainers import SortedList, SortedSet, SortedDict
class SummaryRanges:

    def __init__(self):
        self.nums = SortedSet()
        
    def addNum(self, value: int) -> None:
        self.nums.add(value)

            
    def getIntervals(self) -> List[List[int]]:
        res  = []
        for n in self.nums:
            if res and res[-1][1] + 1 == n:
                res[-1][1] = n
            else:
                res.append([n, n])
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()