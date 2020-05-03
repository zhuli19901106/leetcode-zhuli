# https://leetcode.com/problems/reducing-dishes/
# O(n^2) DP solution
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        INT_MIN = -(2 ** 31)

        s = satisfaction
        n = len(s)
        s.sort()
        dp = [[0 for j in range(n)] for i in range(n)]

        res = 0
        for i in range(n):
            dp[0][i] = s[i]
            res = max(res, dp[0][i])
        for i in range(1, n):
            cur = INT_MIN
            for j in range(i, n):
                cur = max(cur, dp[i - 1][j - 1])
                dp[i][j] = cur + (i + 1) * s[j]
                res = max(res, dp[i][j])
        return res
