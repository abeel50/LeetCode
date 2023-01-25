class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        
        res = int(math.log2(abs(n)))
        
        return True if n == 2 ** res else False
        