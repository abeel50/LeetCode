class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        sm, j = 0, 0
        
        for i, num in enumerate(nums):
            sm += num
            while sm >= target:
                res = min(res, i - j + 1)
                sm -= nums[j]
                j += 1
        return res if res != float("inf") else 0