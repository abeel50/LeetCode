class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        h = dict.fromkeys(string.ascii_lowercase,0)
        
        for c in sentence:
            h[c] += 1
        return len([True for v in h.values() if v > 0]) == 26
        