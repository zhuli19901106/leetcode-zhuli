# medium
# https://leetcode.com/problems/regions-cut-by-slashes/
# very labor intensive
from collections import deque

class Solution:
    offs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

    def regionsBySlashes(self, grid: List[str]) -> int:
        a = Solution.zoom(grid, 3)
        return Solution.countRegion(a)

    @staticmethod
    def countRegion(a):
        n = len(a)
        m = len(a[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] != 0:
                    continue
                Solution.flood(a, i, j, 0, 2)
                res += 1
        return res

    @staticmethod
    def flood(a, x, y, old_val, new_val):
        n = len(a)
        m = len(a[0])

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        q = deque()
        a[x][y] = new_val
        q.append((x, y))
        while len(q) > 0:
            x, y = q.popleft()
            for off in Solution.offs:
                x1, y1 = x + off[0], y + off[1]
                if not (inbound(x1, y1) and a[x1][y1] == old_val):
                    continue
                a[x1][y1] = new_val
                q.append((x1, y1))

    @staticmethod
    def zoom(a0, z):
        n = len(a0)
        m = len(a0[0])
        a = [[0 for j in range(m * z)] for i in range(n * z)]
        for i in range(n):
            for j in range(m):
                if a0[i][j] == r' ':
                    continue
                if a0[i][j] == '/':
                    for ki in range(z):
                        for kj in range(z):
                            if ki + kj == z - 1:
                                a[i * z + ki][j * z + kj] = 1
                elif a0[i][j] == '\\':
                    for ki in range(z):
                        for kj in range(z):
                            if ki == kj:
                                a[i * z + ki][j * z + kj] = 1
        return a
