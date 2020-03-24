# number-of-recent-calls
from collections import deque

class RecentCounter:
    TIMEOUT = 3000

    def __init__(self):
        self._q = deque()

    def ping(self, t: int) -> int:
        while len(self._q) > 0 and\
            t - self._q[0] > RecentCounter.TIMEOUT:
            self._q.popleft()
        self._q.append(t)
        return len(self._q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)