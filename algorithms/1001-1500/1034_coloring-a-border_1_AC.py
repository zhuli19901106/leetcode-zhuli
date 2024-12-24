# medium
# https://leetcode.com/problems/coloring-a-border/
# flooding with a bit tweaking
class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        offs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        a = grid
        if a[r0][c0] == color:
            return a
        n = len(a)
        m = len(a[0])

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        def flood(x, y, ov, nv):
            nonlocal a

            cnt = 0
            for off in offs:
                x1, y1 = x + off[0], y + off[1]
                if inbound(x1, y1) and (a[x1][y1] == ov or a[x1][y1] < 0):
                    cnt += 1
            a[x][y] = -nv if cnt < 4 else -ov
            for off in offs:
                x1, y1 = x + off[0], y + off[1]
                if inbound(x1, y1) and a[x1][y1] == ov:
                    flood(x1, y1, ov, nv)

        flood(r0, c0, a[r0][c0], color)
        for i in range(n):
            for j in range(m):
                if a[i][j] < 0:
                    a[i][j] = -a[i][j]
        return a
