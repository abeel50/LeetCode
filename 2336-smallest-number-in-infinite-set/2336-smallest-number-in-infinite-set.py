from sortedcontainers import SortedSet

class SmallestInfiniteSet:

    def __init__(self):
        self.nums = SortedSet(range(1,1001))
        
    def popSmallest(self) -> int:
        res = self.nums[0]
        self.nums.discard(res)
        return res


    def addBack(self, num: int) -> None:
        if num not in self.nums:
            self.nums.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)