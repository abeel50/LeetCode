class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small, large = nums[0], nums[0]
        # find min and max in one iteration         
        for i in nums[1:]:
            if i > large:
                large = i
            if i < small:
                small =i
        #if both number are same
        if small == large:
            return small
        gcd = 1
        for n in range(1, large + 1):
            if small % n == 0 and large % n == 0:
                gcd = n
        return gcd
        
            
                                                                                                                                                
        