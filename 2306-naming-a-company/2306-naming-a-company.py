class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        
        wordMap = defaultdict(set)
        
        for w in ideas:
            wordMap[w[0]].add(w[1:])
        res = 0
        for c1 in wordMap:
            for c2 in wordMap:
                if c1 == c2: continue
                intersect = len([True for w in wordMap[c1] if w in wordMap[c2]])
                
                distinct1, distinct2 = len(wordMap[c1]) - intersect, len(wordMap[c2]) - intersect
                res += distinct1 * distinct2
        return res
                
        
        