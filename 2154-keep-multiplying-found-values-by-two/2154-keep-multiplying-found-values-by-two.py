class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        h = defaultdict(int)
        
        for i,n in enumerate(nums):
            h[n] = i
        
        while original in h:
            original *= 2
        return original
            
            
        