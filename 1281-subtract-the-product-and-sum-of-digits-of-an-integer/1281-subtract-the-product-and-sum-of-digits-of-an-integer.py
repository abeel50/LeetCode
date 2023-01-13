class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        p ,s = 1,0
        for i in str(n):
            p , s = p * int(i) , s + int(i)
        return p-s
            
        