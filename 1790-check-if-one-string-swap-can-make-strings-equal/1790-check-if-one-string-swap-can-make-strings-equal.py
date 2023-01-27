class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        idx1 ,idx2 = -1, -1
        for i in range (len(s1)):
            if s1[i] != s2[i]:
                if idx1 == -1:
                    idx1 = i
                elif idx2 == -1:
                    idx2 = i
                else:
                    return False
        
        
        if (idx1 < 0 and idx2 < 0): return True
        if (idx2 < 0): return False
        if (s1[idx1] == s2[idx2] and s1[idx2] == s2[idx1]): return True
        return False  