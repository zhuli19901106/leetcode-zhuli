# https://leetcode.com/problems/last-stone-weight/
from heapq import heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        class Stone:
            def __init__(self, val):
                self.val = val

            def __lt__(self, other):
                return self.val > other.val

            def __eq__(self, other):
                return self.val == other.val

            def __sub__(self, other):
                return Stone(self.val - other.val)

        pq = []
        for x in stones:
            heappush(pq, Stone(x))
        while len(pq) >= 2:
            s1 = heappop(pq)
            s2 = heappop(pq)
            if s1 == s2:
                continue
            heappush(pq, s1 - s2)
        if len(pq) > 0:
            s1 = heappop(pq)
            return s1.val
        else:
            return 0
