class Solution:
    def firstUniqChar(self, s: str) -> int:
        #index, count
        h = dict.fromkeys(string.ascii_lowercase, (0,0))
        
        for i, c in enumerate(s):
            count = h[c][1]
            h[c] =(i, count + 1)
        freqs = sorted(h.values(), key=lambda x: x[0])
        for i ,f in freqs:
            if f == 1:
                return i
        return -1
        