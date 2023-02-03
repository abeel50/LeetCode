class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = [""] * numRows
        numRows -= 1
        for x in range(len(s)):
            # Simulate Zig-Zag Movement
            zigzag[abs((x + numRows) % (2 * numRows) - numRows)] += s[x]
        return "".join(zigzag)