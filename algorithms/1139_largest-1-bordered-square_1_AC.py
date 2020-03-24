# https://leetcode.com/problems/largest-1-bordered-square/
# brute-force
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        g = grid
        n = len(g)
        m = len(g[0])
        dp = [[[0, 0] for j in range(m + 1)] for i in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if g[i][j] == 0:
                    continue
                dp[i + 1][j + 1][0] = dp[i][j + 1][0] + 1
                dp[i + 1][j + 1][1] = dp[i + 1][j][1] + 1
        found = False
        for k in range(min(n, m), 0, -1):
            for i in range(n - k + 1):
                for j in range(m - k + 1):
                    x, y = i + k - 1, j + k - 1
                    if dp[x + 1][y + 1][0] >= k and dp[x + 1][y + 1][1] >= k and\
                        dp[x + 1][j + 1][0] >= k and dp[i + 1][y + 1][1] >= k:
                        found = True
                if found:
                    break
            if found:
                break
        return k * k if found else 0
