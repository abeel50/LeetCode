class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0 #if height list is empty
        
        #two pointer for start and end of list
        l, r = 0 , len(height) - 1
        #maxL max value on Left side of left pointer
        #maxR max value on Right side pf right side of pointer
        maxL, maxR = height[l], height[r]
        water = 0
        while l < r:
            #Move pointer which has Min Value
            if maxL < maxR: 
                l += 1
                maxL = max(maxL, height[l])
                water += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                water += maxR - height[r]
        return water
        