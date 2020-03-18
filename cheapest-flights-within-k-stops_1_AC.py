# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# single source shortest path with limited steps
# Dijkstra with heap optimization
from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        INT_MAX = 2 ** 31 - 1

        g = [{} for i in range(n)]
        for x, y, w in flights:
            g[x][y] = w

        res = [INT_MAX for i in range(n)]
        pq = []
        vst = set()
        vst.add(src)

        res[src] = 0
        heappush(pq, (0, src, 0))
        while len(pq) > 0:
            d, i, st = heappop(pq)
            if st >= K + 1:
                continue
            for i1 in g[i]:
                if i1 in vst:
                    continue
                d1 = d + g[i][i1]
                if d1 < res[i1]:
                    res[i1] = d1
                heappush(pq, (d1, i1, st + 1))
            if len(pq) == 0:
                break
            # mark the new nearest vertex as visited
            i = pq[0][1]
            vst.add(i)
        return res[dst] if res[dst] != INT_MAX else -1
