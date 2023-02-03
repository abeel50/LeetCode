class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewlsHash = dict.fromkeys(jewels, True)
        
        return len([True for s in stones if s in jewlsHash])
        
        