class Solution:
    def compareWords(self, w1, w2, d):
        for j in range(len(w1)):
            # examine the case when words are like ("apple", "app").
            if j >= len(w2): return False
            if w1[j] != w2[j]:
                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    if d[w1[j]] > d[w2[j]]:
                        return False
                    break
        return True
            
            
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1: return True
        h = {}
        for i,c in enumerate(order):
            h[c] = i
            
        for i in range(len(words)-1):
            if not(self.compareWords(words[i], words[i+1], h)):
                return False
    
        return True
        