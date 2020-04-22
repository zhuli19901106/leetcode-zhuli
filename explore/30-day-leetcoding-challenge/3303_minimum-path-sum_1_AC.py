# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3303/
# 1AC
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        g = grid
        n = len(g)
        m = len(g[0]) if n > 0 else 0
        if n == 0 or m == 0:
            return 0
        for i in range(1, n):
            g[i][0] += g[i - 1][0]
        for j in range(1, m):
            g[0][j] += g[0][j - 1]
        for i in range(1, n):
            for j in range(1, m):
                g[i][j] += min(g[i - 1][j], g[i][j - 1])
        return g[n - 1][m - 1]
