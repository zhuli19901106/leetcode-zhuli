# easy
# https://leetcode.com/problems/surface-area-of-3d-shapes/
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        g = grid
        n = len(g)
        m = len(g[0])

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        res = 0
        offsets = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        for i in range(n):
            for j in range(m):
                if g[i][j] == 0:
                    continue
                res += 2
                for off in offsets:
                    i1 = i + off[0]
                    j1 = j + off[1]
                    if not inbound(i1, j1):
                        res += g[i][j]
                    else:
                        res += max(0, g[i][j] - g[i1][j1])
        return res
