# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
# a bit tricky, do BFS on edges, not vertices
from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        roads.sort(key=lambda x: x[2])
        g = {}
        for x, y, w in roads:
            if not x in g:
                g[x] = {}
            if not y in g:
                g[y] = {}
            g[x][y] = w
            g[y][x] = w

        res = {}
        for x, y, _ in roads:
            if x in res or y in res:
                continue

            self.traverse(x, g, res)

            if 1 in res and n in res:
                break

        return res[1]

    def traverse(self, x0, g, res):
        if x0 in res:
            return

        min_w = -1

        q = deque()
        vst = set()

        q.appendleft(x0)
        while len(q) > 0:
            x = q.pop()
            if x in vst:
                continue

            for y in g[x]:
                if min_w == -1 or min_w > g[x][y]:
                    min_w = g[x][y]
                q.appendleft(y)
            vst.add(x)

        for x in vst:
            res[x] = min_w
