class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        checked = set()
        res = 0
        for n in nums:
            if n - diff in checked and n - (diff * 2) in checked:
                res += 1
            checked.add(n)
        return res                        
        