# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/
from collections import deque

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        g = grid
        n, m = len(g), len(g[0])
        res = 0
        while True:
            found = False
            for i in range(n):
                for j in range(m):
                    if g[i][j] <= 0:
                        continue
                    res = max(res, self.search(g, i, j))
                    found = True
            if not found:
                break

        return res

    def search(self, g, x0, y0):
        OFFS = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

        n, m = len(g), len(g[0])

        q = deque()
        res = 0

        q.appendleft((x0, y0))
        while len(q) > 0:
            x, y = q.pop()
            if g[x][y] > 0:
                res += g[x][y]
            g[x][y] = -1

            for dx, dy in OFFS:
                x1, y1 = x + dx, y + dy
                if x1 < 0 or x1 > n - 1 or y1 < 0 or y1 > m - 1:
                    continue
                if g[x1][y1] <= 0:
                    continue
                q.appendleft((x1, y1))

        return res
