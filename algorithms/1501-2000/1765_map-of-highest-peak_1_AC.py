# medium
# https://leetcode.com/problems/map-of-highest-peak/
from collections import deque

class Solution:
    OFFS = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        g = isWater
        n = len(g)
        m = len(g[0])

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        res = [[-1 for j in range(m)] for i in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if g[i][j] != 1:
                    continue

                res[i][j] = 0
                q.append((i, j, 0))

        while len(q) > 0:
            i, j, cur = q.popleft()
            for ox, oy in self.OFFS:
                i1, j1 = i + ox, j + oy
                if not inbound(i1, j1) or res[i1][j1] != -1:
                    continue

                res[i1][j1] = cur + 1
                q.append((i1, j1, cur + 1))

        return res
