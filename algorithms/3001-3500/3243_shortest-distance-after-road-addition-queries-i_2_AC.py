# medium
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/
# only do BFS starting from y when [x,y] is added
from collections import deque

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = {}
        for i in range(n - 1):
            g[i] = set()
            g[i].add(i + 1)
        g[n - 1] = set()

        d = [i for i in range(n)]

        res = []
        for x, y in queries:
            if not y in g[x]:
                g[x].add(y)

            d[y] = min(d[y], d[x] + 1)
            self.search(g, d, y)
            res.append(d[n - 1])

        return res

    def search(self, g, d, x):
        q, vst = deque(), set()

        vst.add(x)
        q.appendleft((x, d[x]))
        while len(q) > 0:
            x, cur = q.pop()
            if d[x] > cur:
                d[x] = cur

            for y in g[x]:
                if y in vst:
                    continue
                if d[y] <= cur + 1:
                    continue

                vst.add(y)
                q.appendleft((y, cur + 1))
