class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        def rec(arr):
            if len(arr) == 1:
                return arr[0]
            
            res = []
            for i in range(len(arr) - 1):
                res.append((arr[i]+arr[i+1]) % 10)
            return rec(res)
        
        return rec(nums)
            
        