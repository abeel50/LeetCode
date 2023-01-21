class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        mx = max(nums)
        idx = 0
        for i,n in enumerate(nums):
            if n == mx:
                idx = i
            if n != mx and n*2 > mx:
                return -1
        return idx
                
                
        