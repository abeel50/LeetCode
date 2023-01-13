class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        mx = float('-inf')
        
        for i in range(len(arr)-1,-1,-1):
            if i!= len(arr) -1:
                temp = arr[i]
                arr[i] = mx
                if temp > mx:
                    mx = temp
            else:
                if arr[i] > mx:
                    mx = arr[i]
                arr[i] = -1
            

        return arr
            