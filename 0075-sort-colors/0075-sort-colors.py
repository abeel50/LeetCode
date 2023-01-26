class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = defaultdict(int)
        
        for n in nums:
            d[n] += 1
        
        j = 0
        for i in range(3):
            while d[i] > 0:
                nums[j] = i
                d[i] -= 1
                j+=1
        
        