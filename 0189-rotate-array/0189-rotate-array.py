class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or k == 0 or len(nums) == k or nums.count(nums[0]) == len(nums):
            return
        else:
            new_A = nums[:]
            for i in range(len(nums)):
                j = ( i + (k % len(nums))) % len(nums)
                nums[j] = new_A[i]
        