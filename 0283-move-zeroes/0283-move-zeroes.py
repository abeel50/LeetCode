class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i ,k =0 ,0
        
        while i < len(nums):
            if nums[i] == 0:
                k = i
                while k < len(nums) and nums[k] == 0 :
                    k += 1
                if k < len(nums):
                    nums[i], nums[k] = nums[k], nums[i]
            i += 1
        
        
        
        