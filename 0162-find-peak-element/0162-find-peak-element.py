class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        idx = 0
        if len(nums) == 1: return idx
        for i in range(len(nums)):
            if i == 0 and nums[i] > nums[i+1]:
                return i
            elif i== len(nums) -1 and nums[i] > nums[i-1]:
                return i
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        return idx
        