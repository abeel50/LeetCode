class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        
        h_rans = dict.fromkeys(string.ascii_lowercase, 0)
        h_magz = dict.fromkeys(string.ascii_lowercase, 0)
        for c in ransomNote:
            h_rans[c] += 1
        for c in magazine:
            h_magz[c] += 1
            
        for c in set(ransomNote):
            if h_rans[c] > h_magz[c]:
                return False
        return True
        