class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        distance = 0
        
        for num1 in arr1:
            is_qualify = True
            for num2 in arr2:
                diff = abs(num1 - num2)
                
                if diff <= d:
                    is_qualify = False
                    break
                
            if is_qualify:
                distance += 1
        return distance

        