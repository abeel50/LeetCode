class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        n = (high - low) // 2
        
        # if either high or low is odd
        if (high % 2 != 0 or low % 2 != 0):
            return n + 1
        return n
            
        
        