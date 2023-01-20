class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for c in s:
            asc = ord(c)
            if asc >= 65 and asc <= 90:
                res += chr(97 + (asc - 65))
            else:
                res += c
        return res
        