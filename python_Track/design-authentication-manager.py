class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.token = {}
        self.totalTime = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token and self.token[tokenId] + self.totalTime > currentTime:
            self.token[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ct = 0
        for v  in self.token.values():
            if v + self.totalTime > currentTime:
                ct+=1
        return ct


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)