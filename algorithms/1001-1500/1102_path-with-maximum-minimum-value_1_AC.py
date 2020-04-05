# https://leetcode.com/problems/path-with-maximum-minimum-value/
# https://leetcode.com/problems/path-with-maximum-minimum-value/discuss/530766/Python-3-DFS%2BHeap
# the key is in getting the idea of heap, not quite intuitive
from heapq import heappush, heappop

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        offs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        a = A
        n = len(a)
        m = len(a[0])

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        vs = [[False for j in range(m)] for i in range(n)]
        pq = []

        vs[0][0] = True
        heappush(pq, (-a[0][0], 0, 0))
        while len(pq) > 0:
            v, x, y = heappop(pq)
            v = -v
            if x == n - 1 and y == m - 1:
                return v
            for off in offs:
                x1, y1 = x + off[0], y + off[1]
                if not inbound(x1, y1) or vs[x1][y1]:
                    continue
                vs[x1][y1] = True
                heappush(pq, (-min(v, a[x1][y1]), x1, y1))
