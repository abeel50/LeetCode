class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) > len(s): return False
        
        h_t = dict.fromkeys(string.ascii_lowercase, 0)
        h_s = dict.fromkeys(string.ascii_lowercase, 0)
        for c in s:
            h_s[c] += 1
        for c in t:
            h_t[c] += 1
            
        for c in string.ascii_lowercase:
            if h_t[c] != h_s[c]:
                return False
        return True
        