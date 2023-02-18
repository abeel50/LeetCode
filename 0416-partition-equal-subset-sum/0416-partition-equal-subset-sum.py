class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 ==1: return False
        
        dp = set([0])
        target = sum(nums) // 2
        
        for i in range(len(nums)-1,-1,-1):
            nextDp = set()
            for t in dp:
                nextDp.add(t + nums[i])
                nextDp.add(t)
            dp = nextDp
        return True if target in dp else False
            