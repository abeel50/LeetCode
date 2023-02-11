class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        def rec(arr):
            if len(arr) == 1:
                return arr[0]            
            for i in range(len(arr) - 1):
                arr[i] = (arr[i] + arr[i + 1]) % 10
            arr.pop()
            return rec(arr)
        
        return rec(nums)
            
        