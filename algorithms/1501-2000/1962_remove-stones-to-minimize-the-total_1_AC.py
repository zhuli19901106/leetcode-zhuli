# https://leetcode.com/problems/remove-stones-to-minimize-the-total/
from heapq import heappush, heappop

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = []
        for x in piles:
            heappush(pq, -x)

        for i in range(k):
            x = -heappop(pq)
            if x == 0:
                break
            x = (x + 1) // 2
            heappush(pq, -x)

        res = 0
        while len(pq) > 0:
            res -= heappop(pq)

        return res
