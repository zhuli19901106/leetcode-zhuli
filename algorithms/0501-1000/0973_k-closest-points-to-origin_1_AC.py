# medium
# https://leetcode.com/problems/k-closest-points-to-origin/submissions/
from heapq import heappush, heappop

class HeapNode:
    def __init__(self, p, d):
        self.p = p
        self.d = d

    def __lt__(self, o):
        return self.d > o.d

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pq = []
        n = len(points)
        k = min(K, n)
        for i in range(k):
            p = points[i]
            d = p[0] ** 2 + p[1] ** 2
            heappush(pq, HeapNode(p, d))
        for i in range(k, n):
            p = points[i]
            d = p[0] ** 2 + p[1] ** 2
            if pq[0].d > d:
                heappop(pq)
                heappush(pq, HeapNode(p, d))
        res = []
        while len(pq) > 0:
            res.append(heappop(pq).p)
        return res
