# easy
# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/
from heapq import heappush, heappop

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = []
        for i, x in enumerate(nums):
            heappush(pq, (x, i))
        for i in range(k):
            x, i = heappop(pq)
            heappush(pq, (x * multiplier, i))

        n = len(nums)
        res = [0 for i in range(n)]
        while len(pq) > 0:
            x, i = heappop(pq)
            res[i] = x
        return res
