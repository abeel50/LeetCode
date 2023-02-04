class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = set()
        for n in nums:
            res.add(n)
            res.add(int(str(n)[::-1]))
        return len(res)
        
        