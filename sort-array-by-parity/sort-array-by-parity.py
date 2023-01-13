class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return ([x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1])

        