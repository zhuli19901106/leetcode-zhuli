# medium
# https://leetcode.com/problems/shortest-path-with-alternating-colors/
# 1AC, alternating BFS
from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        INT_MAX = 2 ** 31 - 1

        def buildGraph(ae, n):
            g = [set() for i in range(n)]
            for x, y in ae:
                g[x].add(y)
            return g

        g = []
        g.append(buildGraph(red_edges, n))
        g.append(buildGraph(blue_edges, n))
        mm = {}

        q = deque()
        mm[(0, 0)] = 0
        q.append((0, 0))
        mm[(0, 1)] = 0
        q.append((0, 1))
        while len(q) > 0:
            x, f = q.popleft()
            d = mm[(x, f)]
            for x1 in g[1 - f][x]:
                if (x1, 1 - f) in mm:
                    continue
                mm[(x1, 1 - f)] = d + 1
                q.append((x1, 1 - f))
        res = [-1 for i in range(n)]
        for i in range(n):
            min_dist = INT_MAX
            for f in (0, 1):
                if (i, f) in mm:
                    min_dist = min(min_dist, mm[(i, f)])
            if min_dist != INT_MAX:
                res[i] = min_dist
        return res
