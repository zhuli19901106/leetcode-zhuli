# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/
from heapq import heappush, heappop

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = []
        for i, g in enumerate(gifts):
            heappush(pq, -g)
        for i in range(k):
            g = -heappop(pq)
            g = int(g ** 0.5)
            heappush(pq, -g)
        return -sum(pq)
