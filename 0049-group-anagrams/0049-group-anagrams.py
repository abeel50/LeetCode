class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map count of each string to => word
        # [e:1, a:1, t:1] = ["word"]
        res = defaultdict(list)
        
        for s in strs:
            # [a,b,c, ... ,z]
            freq = [0] * 26
            
            for c in s:
                freq[ord(c) - ord("a")] += 1
            res[tuple(freq)].append(s)
        return res.values()