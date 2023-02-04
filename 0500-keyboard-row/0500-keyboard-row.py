class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        for r in rows:
            for w in words:
                if len([True for c in w if c.lower() in r]) == len(w):
                    res.append(w)
        return res