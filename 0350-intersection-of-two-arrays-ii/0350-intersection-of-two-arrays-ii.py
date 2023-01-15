class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # return [value for value in nums1 if value in nums2]
        h1 ,h2 = defaultdict(int), defaultdict(int)

        for i in nums1:
            h1[i] += 1
        for i in nums2:
            h2[i] +=1
        res = []
        
        for k,v in h1.items():
            if k in h2:
                m = min(h1[k], h2[k])
                res.extend([k] *m)
        return res
            
        