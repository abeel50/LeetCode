class Solution:
    def fib(self, n: int) -> int:        
        fib0, fib1 = 0, 1
        
        if n == 0: return 0
        if n == 1: return 1 
        
        for i in range(2, n + 1):
            temp = fib1
            fib1 = fib0 + fib1
            fib0 = temp
        return fib1
        
        