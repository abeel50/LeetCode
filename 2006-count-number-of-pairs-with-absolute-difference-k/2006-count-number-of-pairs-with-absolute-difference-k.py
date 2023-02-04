class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0        
        for i, n in enumerate(nums):
            for j in range(i+1, len(nums)):
                n2 = nums[j]
                if abs(n - n2) == k:
                    res += 1
        return res