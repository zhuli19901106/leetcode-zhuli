# medium
# https://leetcode.com/problems/minimum-path-cost-in-a-grid/
# typical

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        INF = 1 << 31 - 1
        m, n = len(grid), len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]

        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(1, m):
            for j in range(n):
                min_val = INF
                for j1 in range(n):
                    cur = dp[i - 1][j1] + moveCost[grid[i - 1][j1]][j] + grid[i][j]
                    min_val = min(min_val, cur)
                dp[i][j] = min_val

        res = INF
        for j in range(n):
            res = min(res, dp[m - 1][j])

        return res
