class Solution:
    def freqAlphabets(self, s: str) -> str:
        h = {}
        
        # build hash map for mapping
        for i in range(1, 27):
            if i < 10:
                h[str(i)] = string.ascii_lowercase[i-1]
            else:
                h[str(i) + "#"] = string.ascii_lowercase[i-1]
    
        # result and index
        res, i = "", 0
        
        while i < len(s):
            lookAhead = i + 2
            if lookAhead < len(s):
                if s[lookAhead] == "#":
                    key = s[i:lookAhead +1]
                    res += h[key]
                    i = lookAhead + 1
                else:
                    res += h[s[i]]
                    print(res)
                    i += 1
            else:
                res += h[s[i]]
                i += 1
                
            
            
        return res
        