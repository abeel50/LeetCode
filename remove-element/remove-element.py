class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = l = len(nums)
        
        for i in range(k):
            if nums[i] != val:
                nums.append(nums[i])
                k -= 1
        for i in range(l):
            nums.pop(0)
       
        return l-k
               
                
                