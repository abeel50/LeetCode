class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l, r = 0, int(c ** 0.5)
        while l <= r:
            lhs = l*l + r*r
            if lhs == c: return True
            if lhs < c: l += 1
            else: r -= 1
        return False
            
        
        
        