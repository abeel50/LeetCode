class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #left sum is sum of Left items from index i
        #right sum od sum of items from index i
        sumLeft, sumRight = [0] * len(nums), [0] * len(nums)

        #computes left sums and right sums
        for i in range(len(nums)):
            if i == 0 :
                sumLeft[i] = 0
                sumRight[i] = sum(nums[1:])
            else:
                sumLeft[i] = sumLeft[i-1] + nums[i-1]
                sumRight[i] =  sumRight[i-1] - nums[i]
                
            if i == len(nums) - 1:
                sumRight[i] = 0


        for i in range(len(sumLeft)):
            if sumRight[i] == sumLeft[i]: #if index values match then return index
                return i
        return -1
        