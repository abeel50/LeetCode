class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        for i in str(bin(n)[2:]):
            if int(i) == 1:
                c += 1
        return c