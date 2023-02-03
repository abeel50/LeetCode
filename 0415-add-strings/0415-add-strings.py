class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        
        while i > -1 or j > -1 or carry == 1:
            if i > -1 and j > -1:
                temp = int(num1[i]) + int(num2[j]) + carry
                i -= 1
                j -= 1

            elif i > -1:
                temp = int(num1[i]) + carry
                i -= 1

            elif j > -1:
                temp = int(num2[j]) + carry
                j -= 1
            else:
                temp = carry
            carry = 0
            if temp > 9:
                carry = 1
            res.insert(0, str(temp)[-1])
        
        return "".join(res)
                