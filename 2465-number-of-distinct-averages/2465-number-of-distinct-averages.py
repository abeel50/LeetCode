class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        averages = defaultdict(bool)
        
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            avg = (nums[l] + nums[r] ) / 2
            averages[avg] = True
            l += 1
            r -= 1
        return len(averages.keys())