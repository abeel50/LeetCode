class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(int)
        
        for n in nums:
            d[n] += 1
            if d[n] > 1:
                return n
            
        