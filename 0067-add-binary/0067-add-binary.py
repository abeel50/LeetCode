class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a) - 1, len(b) - 1
        
        c = 0
        while i >= 0 or j >= 0 or c == 1:
            temp = 0
            if i >= 0 and j >= 0:
                temp = int(a[i]) + int(b[j]) + c
            elif i >= 0:
                temp = int(a[i]) + c
            elif j >= 0:
                temp = int(b[j]) + c
            else:
                temp = c      
            c = 0
            if temp < 2:
                res.append(str(temp))
            elif temp == 2:
                res.append("0")
                c = 1
            else:
                res.append("1")
                c = 1
            i -= 1
            j -= 1
        return "".join(res[::-1])
            