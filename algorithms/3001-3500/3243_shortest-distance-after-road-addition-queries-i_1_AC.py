# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/
# just do BFS for each query
from collections import deque

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = {}
        for i in range(n - 1):
            g[i] = set()
            g[i].add(i + 1)

        q, vst = deque(), set()
        res = []
        for x, y in queries:
            if not y in g[x]:
                g[x].add(y)

            vst.add(0)
            q.appendleft((0, 0))
            while len(q) > 0:
                x, d = q.pop()
                if x == n - 1:
                    res.append(d)
                    break

                for y in g[x]:
                    if y in vst:
                        continue
                    vst.add(y)
                    q.appendleft((y, d + 1))
            q.clear()
            vst.clear()

        return res
