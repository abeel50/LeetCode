class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res  = []
        subset = []
        
        def backTrack(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            # with current number
            subset.append(nums[i])
            backTrack(i + 1)
            
            #withput including current number
            subset.pop()
            # to avoid duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backTrack(i + 1)
            
        backTrack(0)
        return res
        