class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, value in enumerate(nums):
            if target - value in d:
                return [d[target - value], i]
            else:
                d[value] = i
            
        