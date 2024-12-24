# medium
# https://leetcode.com/problems/design-authentication-manager/
# it seems rather slow, isn't it
from sortedcontainers import SortedDict

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.mm_time = SortedDict()
        self.mm_token = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.mm_token:
            return

        expire = currentTime + self.ttl
        self.mm_token[tokenId] = expire

        if not expire in self.mm_time:
            self.mm_time[expire] = set()
        self.mm_time[expire].add(tokenId)

    def renew(self, tokenId: str, currentTime: int) -> None:
        if not tokenId in self.mm_token:
            # not found
            return

        expire = self.mm_token[tokenId]
        if expire <= currentTime:
            # expired
            return

        self._remove(tokenId)
        self.generate(tokenId, currentTime)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        for t in reversed(self.mm_time):
            if t <= currentTime:
                break
            res += len(self.mm_time[t])

        return res

    def _remove(self, tokenId: str) -> None:
        if not tokenId in self.mm_token:
            return

        expire = self.mm_token[tokenId]
        del self.mm_token[tokenId]

        st = self.mm_time[expire]
        if len(st) > 1:
            st.remove(tokenId)
        else:
            del self.mm_time[expire]

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)