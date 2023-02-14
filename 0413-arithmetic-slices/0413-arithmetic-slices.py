class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [None] * (len(nums) - 1)
        
        for i in range(1, len(nums)):
            dp[i-1] = nums[i] - nums[i-1]
        
        res, m = 0, 1
        
        for i in range(1, len(dp)):
            if dp[i] == dp[i-1]:
                res += m
                m += 1
            else:
                m = 1
        return res    