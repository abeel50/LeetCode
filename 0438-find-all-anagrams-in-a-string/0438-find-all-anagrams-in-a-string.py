class Solution:
    
    def isAnagram(self, hs, hp):
        for k,v in hs.items():
            if k not in hp:
                return False
            if v != hp[k]:
                return False
        return True
        
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res =[]
        if len(p) > len(s): return res
        hp = defaultdict(int)
        hs =  defaultdict(int)
        
        for c in p:
            hp[c] += 1
        for c in s[:len(p)]:
            hs[c] += 1
            
        if self.isAnagram(hs,hp):
            res.append(0)
        
        hs[s[0]] -= 1
        if hs[s[0]] == 0:
            del hs[s[0]]
            
        for i in range(1, len(s) - len(p) + 1):
            start = s[i]
            end = s[ i + len(p) - 1]
            
            hs[end] += 1
            if self.isAnagram( hs, hp):
                res.append(i)

            hs[start] -= 1
            if hs[start] == 0:
                del hs[start]
            
        return res        