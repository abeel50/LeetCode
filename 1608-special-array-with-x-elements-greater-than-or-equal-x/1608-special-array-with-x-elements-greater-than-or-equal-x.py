class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(0,len(nums) + 1):
            count = len([i for i in nums if i >= x])
            if count == x:
                return x
        return -1
                
                
            
        