class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        h = defaultdict(int)
        res = set()
        for n in nums:
            h[n] += 1
            if h[n] > 1:
                res.add(n)
        return res
        