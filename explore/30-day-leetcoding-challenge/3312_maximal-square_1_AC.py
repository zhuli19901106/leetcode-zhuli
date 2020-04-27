# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3312/
# 1AC, DP solution.
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        a = matrix
        n = len(a)
        m = len(a[0]) if n > 0 else 0
        if n == 0 or m == 0:
            return 0

        res = 0
        dp = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                dp[i][j] = int(a[i][j])
                if a[i][j] == '0':
                    continue
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                res = max(res, dp[i][j])
        res = res ** 2
        return res
