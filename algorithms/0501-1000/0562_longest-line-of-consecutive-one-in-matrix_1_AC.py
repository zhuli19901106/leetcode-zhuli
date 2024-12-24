# medium
# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
# O(n * m) DP solution 
class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        offs = [(-1, 0), (0, -1), (-1, -1), (-1, +1)]
        a = M
        n = len(a)
        if n == 0:
            return 0
        m = len(a[0])
        if m == 0:
            return 0

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        res = 0
        dp = [[0 for j in range(m)] for i in range(n)]
        for off in offs:
            for i in range(n):
                for j in range(m):
                    i1, j1 = i + off[0], j + off[1]
                    dp[i][j] = a[i][j]
                    if a[i][j] == 1 and inbound(i1, j1):
                        dp[i][j] += dp[i1][j1]
                    res = max(res, dp[i][j])
        return res
