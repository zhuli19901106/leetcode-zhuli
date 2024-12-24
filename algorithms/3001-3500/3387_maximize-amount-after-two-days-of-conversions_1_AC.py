# medium
# https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/
# horribly lengthy and unnecessary
from collections import deque

class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        g1 = self.constructGraph(pairs1, rates1)
        g2 = self.constructGraph(pairs2, rates2)

        res = 1.0
        x0 = initialCurrency
        dist1 = self.search(x0, g1)
        for y in dist1:
            dist2 = self.search(y, g2)
            if x0 in dist2:
                res = max(res, dist1[y] * dist2[x0])\

        return res

    def constructGraph(self, ps, rs):
        ne = len(ps)
        g = {}
        for i in range(ne):
            x, y = ps[i]
            r = rs[i]
            if not x in g:
                g[x] = {}
            if not y in g:
                g[y] = {}

            g[x][y] = r
            g[y][x] = 1 / r

        return g

    def search(self, x0, g):
        dist = {}
        dist[x0] = 1.0
        if not x0 in g:
            return dist

        q = deque()
        q.appendleft((x0, dist[x0]))
        while len(q) != 0:
            x, r = q.pop()

            for y in g[x]:
                if y in dist:
                    continue
                dist[y] = r * g[x][y]
                q.appendleft((y, dist[y]))

        return dist
