class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedHash = dict.fromkeys(allowed, True)
        res = 0
        for w in words:
            if all([False for c in w if c not in allowedHash]):
                res += 1
        return res
        