class Token:
    def __init__(self, currTime, timeToLive):
        self.exp = currTime + timeToLive
        
    def isExpired(self, t):
        return t >= self.exp
    
    def renewToken(self, t, timeToLive):
        if self.isExpired(t): return
        self.exp = t + timeToLive

        
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        newToken = Token(currentTime, self.timeToLive)
        self.tokens[tokenId] = newToken

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens: return
        self.tokens[tokenId].renewToken(currentTime, self.timeToLive)
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return len([True for k, v in self.tokens.items() if not v.isExpired(currentTime)])
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)