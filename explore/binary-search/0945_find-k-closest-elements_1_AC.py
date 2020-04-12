# https://leetcode.com/explore/learn/card/binary-search/135/template-iii/945/
# max heap
from heapq import heappush, heappop

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []
        for v in arr:
            heappush(pq, (-abs(v - x), -v))
            if len(pq) > k:
                heappop(pq)
        res = [-x[1] for x in pq]
        res.sort()
        return res
