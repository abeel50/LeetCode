class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0,1,1]
        if n < 3:
            return tri[n]
        
        for i in range(3, n + 1):
            tri.append(sum(tri))
            tri.pop(0)
        return tri[-1]
            
        