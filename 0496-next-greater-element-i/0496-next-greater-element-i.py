class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = defaultdict(int)
        res =[]
        for i,n in enumerate(nums2):
            h[n] = i
        for n2 in nums1:
            mx =-1
            for k in range(h[n2] + 1 , len(nums2)):
                if nums2[k] > n2:
                    mx = nums2[k]
                    break
            res.append(mx)
        return res
        