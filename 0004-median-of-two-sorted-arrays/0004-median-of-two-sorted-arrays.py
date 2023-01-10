class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = [0] * (len(nums1) + len(nums2))
        i,j,k =0,0,0
        while k < len(nums1) + len(nums2):
            if i == len(nums1) or j == len(nums2):
                break
            if nums1[i] < nums2[j]:
                n[k]  = nums1[i]
                k +=1
                i+=1
            else:
                n[k] = nums2[j]
                j+=1
                k+=1

        while i < len(nums1):
            n[k] = nums1[i]
            i+=1
            k+=1
        while j < len(nums2):
            n[k] = nums2[j]
            j+=1
            k+=1
        
        mid = len(n) // 2
        if len(n) % 2 == 0:
            return ( n[mid] + n[mid-1] )/ 2.0
        else:
            return n[mid]

