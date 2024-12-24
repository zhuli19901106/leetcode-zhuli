# medium
# https://leetcode.com/problems/minimum-cost-to-connect-sticks/
# 1AC, min heap
from heapq import heappush, heappop

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        pq = []
        for x in sticks:
            heappush(pq, x)
        res = 0
        while len(pq) > 1:
            x = heappop(pq)
            y = heappop(pq)
            res += x + y
            heappush(pq, x + y)
        return res
