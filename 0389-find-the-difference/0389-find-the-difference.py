class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        h1 = defaultdict(int)
        h2 = defaultdict(int)
        
        for c in s:
            h1[c]+=1 

        for c in t:
            h2[c]+=1 
            
        for k,v in h2.items():
            if k in h1 and v == h1[k]:
                continue
            return k
        
        
        