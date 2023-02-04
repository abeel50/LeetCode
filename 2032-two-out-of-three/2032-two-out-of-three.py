class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums = set(nums1 + nums2 + nums3)
        res = []
        for n in nums:
            if (n in nums1 and n in nums2) or (n in nums1 and n in nums3) or (n in nums2 and n in nums3):
                res.append(n)
        return res