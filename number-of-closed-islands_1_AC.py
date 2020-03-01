# https://leetcode.com/problems/number-of-closed-islands/
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        offs = [(+1, 0), (-1, 0), (0, +1), (0, -1)]

        a = grid
        n = len(a)
        m = len(a[0])

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        def flood(x, y, old_val, new_val):
            a[x][y] = new_val
            for off in offs:
                x1, y1 = x + off[0], y + off[1]
                if inbound(x1, y1) and a[x1][y1] == old_val:
                    flood(x1, y1, old_val, new_val)

        for i in range(n):
            if a[i][0] == 0:
                flood(i, 0, 0, 2)
            if a[i][m - 1] == 0:
                flood(i, m - 1, 0, 2)
        for i in range(m):
            if a[0][i] == 0:
                flood(0, i, 0, 2)
            if a[n - 1][i] == 0:
                flood(n - 1, i, 0, 2)
        res = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == 0:
                    res += 1
                    flood(i, j, 0, 3)
        return res
