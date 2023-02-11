class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        d = dict(zip(string.ascii_uppercase, range(1, 27)))
            
        return sum([(26 ** (len(columnTitle) - 1 - i)) * d[c] for i, c in enumerate(columnTitle)])
        