class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for i in nums:
            d[i] += 1
            if d[i] > (len(nums)) // 2:
                return i