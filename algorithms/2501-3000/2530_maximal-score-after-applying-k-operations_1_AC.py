# medium
# https://leetcode.com/problems/maximal-score-after-applying-k-operations/
# heap it is
from heapq import heappush, heappop

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = []
        for x in nums:
            # for max heap
            heappush(pq, -x)

        res = 0
        for i in range(k):
            x = -heappop(pq)
            res += x
            heappush(pq, -((x + 2) // 3))
        return res
