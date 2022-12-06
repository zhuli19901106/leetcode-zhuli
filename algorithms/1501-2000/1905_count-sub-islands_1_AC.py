# https://leetcode.com/problems/count-sub-islands/
# a bit searching
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        offs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        n, m = len(grid1), len(grid1[0])
        g = [[grid1[i][j] + (grid2[i][j] * 2) for j in range(m)] for i in range(n)]

        def dfs(g, x, y):
            g[x][y] = 1
            for ox, oy in offs:
                x1, y1 = x + ox, y + oy
                if x1 < 0 or x1 > n - 1:
                    continue
                if y1 < 0 or y1 > m - 1:
                    continue
                if not (g[x1][y1] == 2 or g[x1][y1] == 3):
                    continue
                dfs(g, x1, y1)

        for x in range(n):
            for y in range(m):
                if g[x][y] == 2:
                    dfs(g, x, y)

        res = 0
        for x in range(n):
            for y in range(m):
                if g[x][y] == 3:
                    res += 1
                    dfs(g, x, y)

        return res
