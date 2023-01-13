class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:]
        i , j , k = 0,0,0
        
        while i < (m + n) and j < m and k < n:
            if temp[j] < nums2[k]:
                nums1[i] = temp[j]
                j += 1
            else:
                nums1[i] = nums2[k]
                k += 1
            i += 1
        while j < m:
            nums1[i] = temp[j]
            i+=1
            j+=1
        while k < n:
            nums1[i] = nums2[k]
            i+=1
            k+=1
            


        
            
                
            

     