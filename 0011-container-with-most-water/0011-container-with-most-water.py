class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = float('-inf')
        
        #start with two pointers one with start one with end
        start , end = 0 , len(height) - 1
        
        while start < end:
            water = (end - start) * min(height[start],height[end])
            res = max(res, water)
            #Move pointer that is low
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return res
        