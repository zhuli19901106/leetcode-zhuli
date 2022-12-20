# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
# this should be rated medium

class Solution:
    def minInsertions(self, s: str) -> int:
        INF = 10 ** 9 + 7

        n = len(s)
        dp = [[INF for j in range(n)] for i in range(n)]

        for i in range(n):
            dp[i][i] = 0

        for i in range(n - 1):
            dp[i][i + 1] = (0 if s[i] == s[i + 1] else 1)

        for k in range(2, n):
            for i in range(n - k):
                j = i + k
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                dp[i][j] = min(dp[i][j], min(dp[i + 1][j], dp[i][j - 1]) + 1)

        return dp[0][n - 1]
