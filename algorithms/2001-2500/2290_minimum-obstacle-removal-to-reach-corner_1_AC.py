# hard
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
# BFS
from heapq import heappush, heappop

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        OFFS = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

        g = grid
        n, m = len(g), len(g[0])

        res = {}
        pq = []

        res[(0, 0)] = 0
        # it's more convenient to use a min heap
        heappush(pq, (res[(0, 0)], 0, 0))
        while len(pq) > 0 and not (n - 1, m - 1) in res:
            c, x, y = heappop(pq)

            for i in range(4):
                x1, y1 = x + OFFS[i][0], y + OFFS[i][1]
                if x1 < 0 or x1 > n - 1 or y1 < 0 or y1 > m - 1:
                    continue
                if (x1, y1) in res:
                    continue

                c1 = c if g[x1][y1] == 0 else c + 1
                res[(x1, y1)] = c1
                heappush(pq, (c1, x1, y1))

        return res[(n - 1, m - 1)]
