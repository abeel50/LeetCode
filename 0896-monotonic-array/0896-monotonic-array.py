class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec, eq = 0, 0, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
            elif nums[i] < nums[i - 1]:
                dec += 1
            else:
                eq += 1
                
                
        return True if (inc + eq) == len(nums) - 1 or (dec + eq) == len(nums) - 1 else False
        