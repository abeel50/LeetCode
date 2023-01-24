class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        p1, p2 = 0, 0
        res  = 0
        
        while p1 < len(nums1) and p2 < len(nums2):
            # if p1 is larger than p2 
            # as array is in decreasing order 
            # move pointer to next small p1
            if nums1[p1] > nums2[p2]:
                p1 += 1
            else:
                res = max(res, p2 - p1)
                p2 += 1
        return res
                
            
        