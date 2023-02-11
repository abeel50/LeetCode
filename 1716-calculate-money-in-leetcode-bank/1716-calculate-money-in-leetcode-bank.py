class Solution:
    def totalMoney(self, n: int) -> int:
        total , monday = 0 , 1
        cur = monday
        for i in range(1, n + 1):
            total += cur
            cur += 1
            
            if i % 7 == 0:
                monday += 1
                cur = monday
        return total
        