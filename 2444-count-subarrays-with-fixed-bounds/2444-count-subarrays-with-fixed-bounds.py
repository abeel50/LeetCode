class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res, left = 0, 0
        right = [-1] * 2
        for i, x in enumerate(nums):
            if not (minK <= x <= maxK):
                left = i+1
                continue
            if x == minK:
                right[0] = i
            if x == maxK:
                right[1] = i
            res += max(min(right)-left+1, 0)
        return res