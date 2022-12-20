# https://leetcode.com/problems/cherry-pickup-ii/
# it worked

from itertools import product

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        OFFS = list(product([-1, 0, +1], [-1, 0, +1]))

        g = grid
        n, m = len(g), len(g[0])
        dp = [[[-1 for j2 in range(m)] for j1 in range(m)] for i in range(n)]

        def get(i, j1, j2):
            if i < 0 or i > n - 1 or j1 < 0 or j1 > m - 1 or j2 < 0 or j2 > m - 1:
                return -1
            return dp[i][j1][j2]

        dp[0][0][m - 1] = g[0][0] + g[0][m - 1]
        for i in range(1, n):
            for j1 in range(m):
                for j2 in range(m):
                    cur = [get(i - 1, j1 + off[0], j2 + off[1]) for off in OFFS]
                    val = max(cur)
                    if val == -1:
                        continue

                    if j1 == j2:
                        dp[i][j1][j2] = val + g[i][j1]
                    else:
                        dp[i][j1][j2] = val + g[i][j1] + g[i][j2]

        res = 0
        for j1 in range(m):
            for j2 in range(m):
                res = max(res, dp[n - 1][j1][j2])

        return res
