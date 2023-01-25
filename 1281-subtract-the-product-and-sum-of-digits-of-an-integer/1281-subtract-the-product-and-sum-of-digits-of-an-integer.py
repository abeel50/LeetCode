class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p ,s = 1,0
        for i in str(n):
            p , s = p * int(i) , s + int(i)
        return p-s
        