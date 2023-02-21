class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        res = 0
        for i in range(len(s)-1 ,-1, -1):
            if s[i] != "":
                res = len(s[i])
                break
        return res
        