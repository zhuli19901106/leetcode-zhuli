# easy
# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/
from heapq import heappush, heappop

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        pq = [-x for x in sorted(amount, reverse=True)]
        while len(pq) > 0 and pq[-1] == 0:
            pq.pop()

        res = 0
        while len(pq) >= 2:
            x = -heappop(pq)
            y = -heappop(pq)
            res += 1
            if x > 1:
                heappush(pq, -(x - 1))
            if y > 1:
                heappush(pq, -(y - 1))
        if len(pq) > 0 and pq[0] < 0:
            res += -pq[0]

        return res
