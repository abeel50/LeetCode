class Solution:
    def addDigits(self, num: int) -> int:
        if num >= 0 and num <= 9:
            return num
        else:
            return self.addDigits(sum([int(i) for i in str(num) ]))
        
        