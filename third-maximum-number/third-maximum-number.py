class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        def placeMax(arr, n):
            if n > arr[0]:
                arr[2] = arr[1]
                arr[1] = arr[0]
                arr[0] = n
            elif n > arr[1]:
                arr[2] = arr[1]
                arr[1] = n
            elif n > arr[2]:
                arr[2] = n
                
        m = [float('-inf'), float('-inf'), float('-inf')]
        for i in set(nums):
            placeMax(m,i)
        print(m)
        if m[2] == float('-inf'):
            return m[0]
        else:
            return m[2]
                
        