# https://leetcode.com/problems/last-stone-weight/
from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-x for x in stones]
        heapify(pq)
        while len(pq) > 1:
            x = heappop(pq)
            y = heappop(pq)
            if x == y:
                continue
            heappush(pq, -abs(x - y))
        return -heappop(pq) if len(pq) > 0 else 0
