class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        result  = 0
        for i in accounts:
            s = sum(i)
            if s > result:
                result = s
        return result
            
        