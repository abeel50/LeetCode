class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for x in range(n + 1):
            if x == len([i for i in nums if i >= x]):
                return x
        return -1
                
                
            
        