class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = s1.split(" "), s2.split(" ")
        words = set(s1 + s2)
        
        h1, h2 = defaultdict(int), defaultdict(int)
        for w in s1:
            h1[w] += 1
        for w in s2:
            h2[w] += 1
        
        return [w for w in words if (w in h1 and h1[w] == 1 and w not in h2) or (w not in h1 and w in s2 and h2[w] == 1)]
        
        