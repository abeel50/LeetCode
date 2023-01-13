class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums[:]
        d = {}
        j = 0
        for i in range(len(temp)):
            if temp[i] not in d.keys():
                d[temp[i]] = 1
                nums[j] = temp[i]
                j+=1
        return len(d.keys())
            
        