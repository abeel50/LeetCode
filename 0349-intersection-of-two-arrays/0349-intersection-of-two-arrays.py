class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = set(nums1 + nums2)
        res = []
        for n in nums:
            if n in nums1 and n in nums2:
                res.append(n)
        return res