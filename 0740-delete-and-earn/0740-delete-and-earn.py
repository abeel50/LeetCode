from sortedcontainers import SortedDict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = SortedDict()
        
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        nums = list(counts.keys())
        
        earn1, earn2 = 0, 0
        for i in range(len(nums)):
            curEarn = nums[i] * counts[nums[i]]
            temp = earn2
            if i > 0 and nums[i] == nums[i-1] + 1:
                earn2 = max(earn2, curEarn + earn1)
            else:
                earn2 = curEarn + earn2
            earn1 = temp
        return earn2
            
        
    
        
        
        