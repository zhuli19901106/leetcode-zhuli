# hard
# https://leetcode.com/problems/put-marbles-in-bags/
# you know, it's weird to test on people's tricky imagination
# like this problem, some say it's extremely simple
# others just got stuck
# cut k-1 times, every time you add a[i] + a[i + 1] to the total sum
# see? tricky
# I don't think a good engineer should rely on this sort of thinking
from heapq import heappush, heappop

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        ws = weights
        n = len(ws)

        pq = []
        for i in range(n - 1):
            heappush(pq, ws[i] + ws[i + 1])

        min_sm = ws[0] + ws[n - 1]
        for i in range(k - 1):
            min_sm += heappop(pq)

        pq = []
        for i in range(n - 1):
            heappush(pq, -(ws[i] + ws[i + 1]))
        max_sm = ws[0] + ws[n - 1]
        for i in range(k - 1):
            max_sm -= heappop(pq)

        return max_sm - min_sm
