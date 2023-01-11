class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(set(nums)) == 1: return len(nums) * [0]
        
        res = [0] * len(nums)
        for n in range(len(nums)):
            res[n] = sum(i < nums[n] for i in nums)
    
        return res
            
        