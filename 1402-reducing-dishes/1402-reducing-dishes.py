class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        N = len(satisfaction)
        satisfaction.sort(reverse= True)
        preSum, res = 0, 0
        
        print(satisfaction)
        for i in range(N):
            preSum += satisfaction[i]
            if preSum < 0:
                break
            res += preSum
        return res
                
            
            
        