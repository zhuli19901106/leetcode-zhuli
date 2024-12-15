# https://leetcode.com/problems/extra-characters-in-a-string/
# bruteforce DP
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        INT_MAX = (1 << 31) - 1
        n = len(s)
        dp = [[INT_MAX for j in range(n)] for i in range(n)]

        for i in range(n):
            dp[i][i] = 0 if s[i] in dictionary else 1

        dst = set(dictionary)
        for d in range(1, n):
            for i in range(n - d):
                j = i + d
                if s[i: j + 1] in dst:
                    dp[i][j] = 0
                    continue

                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                for k in range(i, j + 1):
                    if k == i:
                        dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                    elif k == j:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
                    else:
                        dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + 1)
        return dp[0][n - 1]
