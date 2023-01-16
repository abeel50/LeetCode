class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        h = dict.fromkeys(string.ascii_lowercase, -1)
        
        for i,l in enumerate(letters):
            h[l] = i
        for k,v in h.items():
            if target < k and v != -1:
                return k
        return letters[0]
            
