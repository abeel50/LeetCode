class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        h = dict.fromkeys(range(1, len(nums) + 1), 0)
        for n in set(nums):
            h[n] += 1
        return [k for k,v in h.items() if v == 0]
            
        