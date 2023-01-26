class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []
        
        self.rec(results, s, "", 0)
        
        return results
    
    def rec(self, results, s, permutation, start):
        if len(permutation) == len(s):    
            results.append(permutation)
            return
        
        if s[start].isalpha():
            self.rec(results, s, permutation + s[start].upper(), start + 1)
            self.rec(results, s, permutation + s[start].lower(), start + 1)            
        else:
            self.rec(results, s, permutation + s[start], start + 1)
        
        