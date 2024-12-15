# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/
# simple DP
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        g = grid
        n, m = len(g), len(g[0])
        dp = [[-1 for j in range(m)] for i in range(n)]

        for i in range(n):
            dp[i][0] = 0
        for j in range(1, m):
            for i in range(n):
                if i > 0 and g[i - 1][j - 1] < g[i][j] and dp[i - 1][j - 1] != -1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                if g[i][j - 1] < g[i][j] and dp[i][j - 1] != -1:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1] + 1)
                if i < n - 1 and g[i + 1][j - 1] < g[i][j] and dp[i + 1][j - 1] != -1:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 1)

        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, dp[i][j])
        return res
