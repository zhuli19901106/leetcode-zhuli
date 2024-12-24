# easy
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/
from heapq import heappush, heappop

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        pq = []
        for x in nums:
            heappush(pq, x)

        res = 0
        while len(pq) > 0:
            if pq[0] >= k:
                break

            x = heappop(pq)
            res += 1
        return res
