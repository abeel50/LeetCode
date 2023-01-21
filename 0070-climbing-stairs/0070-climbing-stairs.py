class Solution:
    def climbStairs(self, n: int) -> int:
        
        steps = [0,1,2,3]
    
        if n < 4: return steps[n]
        
        for i in range(4, n + 1):
            steps.append(steps[i-1] + steps[i-2] )
            
        return steps[-1]
        