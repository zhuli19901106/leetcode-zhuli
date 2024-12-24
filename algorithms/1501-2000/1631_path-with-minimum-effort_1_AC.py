# medium
# https://leetcode.com/problems/path-with-minimum-effort/
# a well-designed problem, variant of Dijkstra
# almost a hard medium
# need a heap to be efficient enough
from heapq import heappush, heappop

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        MAX_VAL = 1e6 + 1
        OFFS = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

        h = heights
        n, m = len(h), len(h[0])

        vst = set()
        dist = {(0, 0): 0}

        # using a queue will TLE
        pq = []
        heappush(pq, (0, (0, 0)))
        while len(pq) > 0:
            d, pos = heappop(pq)
            if pos in vst:
                # processed already
                continue
            vst.add(pos)

            x, y = pos
            for dx, dy in OFFS:
                x1, y1 = x + dx, y + dy
                if x1 < 0 or x1 > n - 1 or y1 < 0 or y1 > m - 1:
                    continue

                if (x1, y1) in vst:
                    continue

                w = abs(h[x][y] - h[x1][y1])
                if (not (x1, y1) in dist) or max(dist[(x, y)], w) < dist[(x1, y1)]:
                    dist[(x1, y1)] = max(dist[(x, y)], w)
                    heappush(pq, (dist[(x1, y1)], (x1, y1)))

        return dist[(n - 1, m - 1)]
