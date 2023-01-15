class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 1
        for n in nums:
            if n == 0: return 0
            if n > 0: p *= 1
            else: p*= -1
        return p
        