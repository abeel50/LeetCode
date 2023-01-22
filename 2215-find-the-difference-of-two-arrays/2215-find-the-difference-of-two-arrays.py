class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        h1 = defaultdict(int)
        h2 = defaultdict(int)
        
        for n in nums1:
            h1[n] += 1
            
        for n in nums2:
            h2[n] += 1
                
        res1 = [k for k in h1.keys() if k not in h2]
        res2 = [k for k in h2.keys() if k not in h1]
        
        return [res1, res2]

    
                
        
        