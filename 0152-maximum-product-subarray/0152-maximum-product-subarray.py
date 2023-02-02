class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # if there is only one lement in list
        res = max(nums)
        curMax, curMin = 1, 1
        
        for n in nums:
            # if num is 0 then reset curMax and curMin
            if n == 0:
                curMax, curMin = 1, 1
                continue
            temp = curMax * n
            curMax = max(temp, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax)
        return res

                
        