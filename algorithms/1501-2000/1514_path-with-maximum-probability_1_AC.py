# medium
# https://leetcode.com/problems/path-with-maximum-probability/
# take -log() and it's weighted shortest path
# in case you forgot Dijkstra after so many years outta college, search for it
# watch for edge cases
from heapq import heappush, heappop
from math import exp, log

EPS = 1e-7

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # process edge data
        g = {}
        ne = len(edges)
        for i in range(ne):
            x, y = edges[i]
            w = -log(succProb[i] + EPS)
            if not x in g:
                g[x] = {}
            if not y in g:
                g[y] = {}
            g[x][y] = w
            g[y][x] = w

        if not (start_node in g and end_node in g):
            return 0.0

        vst = set()
        dist = {start_node: 0.0}

        pq = []
        heappush(pq, (0.0, start_node))
        while len(pq) > 0:
            d, x = heappop(pq)
            if x in vst:
                # processed already
                continue
            vst.add(x)

            for y, w in g[x].items():
                if y in vst:
                    continue
                if (not y in dist) or dist[x] + w < dist[y]:
                    dist[y] = dist[x] + w
                    heappush(pq, (dist[y], y))

            if end_node in vst:
                break

        if not end_node in vst:
            return 0.0
        return exp(-dist[end_node])
