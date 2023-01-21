class Solution:
    def check(self, nums: List[int]) -> bool:
        def isSorted(arr):
            for i in range(1, len(arr)):
                if arr[i-1] > arr[i]:
                    return False
            return True
        
        if isSorted(nums): return True

        for r in range(1, len(nums)):
            res = [0] * len(nums)
            for i in range(len(nums)):
                idx = (i + r) % len(nums)
                res[idx] = nums[i]
            if isSorted(res):
                return True
        return False
            
            
        